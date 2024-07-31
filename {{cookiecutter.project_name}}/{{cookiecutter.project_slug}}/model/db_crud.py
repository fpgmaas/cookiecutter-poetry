"""Mixin for the datbase model

This module contains CRUD support functions for the database model.

Each class functions takes the following arguments:

- model_cls: model class to use
- db_session: a valid datbase session
- A logger object
- a dictionary keyed with the database exception and containing the
    http status code and message in the event of such exception
- The data to be handles

Each API returns either the data resulting from the query or a
JSON response with the http status code and error message in the
case of an exception.

Below is a simple example of "query statement" which can be invoked
to resolve the id by name for example.

.. code-block:: python
    statement = select(SomeDBModel).where(SomeDBModel.name == db_model_id)
    with contextlib.suppress(ValueError):
        statement = select(SomeDBModel).where(SomeDBModel.id == int(location_type_id))

The example below shows how the conversion from db error to http error can be performed.

.. code-block:: python
    db_error_handling = {NoResultFound: DBErrorHandling(
        http_status=http_status.HTTP_404_NOT_FOUND,
        msg=f"LocationType {location_type_id} not found!"
    )}

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

from dataclasses import dataclass
from logging import Logger
from typing import Any

from fastapi import status as http_status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import DatabaseError, InvalidRequestError
from sqlmodel import Session, select

from {{cookiecutter.project_slug}}.api_model.common import PartSnapBaseModel


@dataclass
class DBErrorHandling:
    """A simple dataclass to provide the database error handling.

    Those object shall be indexed by expected database exceptions.
    """

    http_status: int
    msg: str


def create(
    model_cls: PartSnapBaseModel,
    db_session: Session,
    logger: Logger,
    data: PartSnapBaseModel,
    db_error_handling: dict[DatabaseError | InvalidRequestError, DBErrorHandling],
) -> PartSnapBaseModel | JSONResponse:
    """Creates a new record

    This class method commits changes to the database. It automatically marks the
    record creation data and the user on behalf of which the record is created.

    If db_error_handling is specified, it will raise an HTTPException with the appropriate
    HTTP status code and message.

    If a database error occurs and there are not matching object associated to the
    SQLAlchemy exception type in db_error_handling, it will raise HTTP 500 (Server error)

    Parameters
    ----------
    db_session: A valid database session
    logger: Logger instance to use to log information
    data: the data to commit to the database
    db_error_handling: Dictionary of error handling

    Returns
    -------

    PartSnapBaseModel: The result of the datbase transaction
    JSONResponse: A object containing the error
    """
    db_record = model_cls.model_validate(data)
    db_session.add(db_record)
    try:
        db_session.commit()
    except (DatabaseError, InvalidRequestError) as db_error:
        db_session.rollback()
        handler = db_error_handling.get(  # type: ignore[call-overload]
            db_error.__class__,
            DBErrorHandling(
                http_status=http_status.HTTP_500_INTERNAL_SERVER_ERROR,
                msg=f"Failed to create record for {model_cls} {data} - no mapping provided error",
            ),
        )
        logger.exception(handler.msg)
        return JSONResponse(
            status_code=handler.http_status,
            content={"detail": handler.msg},
        )
    db_session.refresh(db_record)
    return db_record


def update(
    model_cls: PartSnapBaseModel,
    db_session: Session,
    logger: Logger,
    query_statement: Any,
    data: PartSnapBaseModel,
    db_error_handling: dict[DatabaseError | InvalidRequestError, DBErrorHandling],
) -> PartSnapBaseModel | JSONResponse | Any:
    """Updates an existing record

    This class method commits changes to the database. It automatically marks the
    record data and the user on behalf of which the record is created.

    If db_error_handling is specified, it will raise an HTTPException with the appropriate
    HTTP status code and message.

    If a database error occurs and there are not matching object associated to the
    SQLAlchemy exception type in db_error_handling, it will raise HTTP 500 (Server error)

    Parameters
    ----------
    model_cls: type of model
    db_session: A valid database session
    logger: Logger instance to use to log information
    data: the data to commit to the database
    db_error_handling: Dictionary of error handling

    Returns
    -------

    PartSnapBaseModel: The result of the database transaction
    JSONResponse: A object containing the error
    """
    table_name = model_cls.__class__.__name__
    logger.info(f"Getting single record from {table_name}")
    try:
        db_record = db_session.exec(query_statement).one()
    except (DatabaseError, InvalidRequestError) as db_error:
        db_session.rollback()
        handler = db_error_handling.get(  # type: ignore[call-overload]
            db_error.__class__,
            DBErrorHandling(
                http_status=http_status.HTTP_404_NOT_FOUND,
                msg=f"Failed to locate record in {table_name} - no mapping provided error",
            ),
        )
        logger.exception(handler.msg)
        return JSONResponse(
            status_code=handler.http_status,
            content={"detail": handler.msg},
        )

    logger.debug(f"Updating {model_cls.__class__.__name__}/{db_record}")
    for k, v in data.items():  # type: ignore[attr-defined]
        if k not in ("id", "PSID", "created_by"):
            db_record.__setattr__(k, v)
    try:
        db_session.add(db_record)
        db_session.commit()
        db_session.refresh(db_record)
    except (DatabaseError, InvalidRequestError) as db_error:
        handler = db_error_handling.get(  # type: ignore[call-overload]
            db_error.__class__,
            DBErrorHandling(
                http_status=http_status.HTTP_422_UNPROCESSABLE_ENTITY,
                msg=f"Could not delete  record for {model_cls} {db_error}",
            ),
        )
        logger.exception(handler.msg)
        db_session.rollback()
        return JSONResponse(
            status_code=handler.http_status,
            content={"detail": handler.msg},
        )
    return db_record


def delete(
    model_cls: PartSnapBaseModel,
    db_session: Session,
    logger: Logger,
    query_statement: Any,
    db_error_handling: dict[DatabaseError | InvalidRequestError, DBErrorHandling],
) -> PartSnapBaseModel | JSONResponse:
    """Deletes a record from the database

    Parameters
    ----------
    db_session: A valid database session
    logger: Logger instance to use to log information
    query_statement: An optional query statement to resolve the record id
    db_error_handling: Dictionary of error handling

    Returns
    -------

    """

    table_name = model_cls.__class__.__name__

    try:
        db_record = db_session.exec(query_statement).one()
    except (DatabaseError, InvalidRequestError) as db_error:
        handler = db_error_handling.get(  # type: ignore[call-overload]
            db_error.__class__,
            DBErrorHandling(
                http_status=http_status.HTTP_404_NOT_FOUND,
                msg=f"Failed to locate record in {table_name} - no mapping provided error",
            ),
        )
        logger.exception(handler.msg)
        return JSONResponse(
            status_code=handler.http_status,
            content={"detail": handler.msg},
        )
    logger.debug(f"Deleting {model_cls.__class__.__name__}/{db_record}")
    try:
        db_session.delete(db_record)
        db_session.commit()
    except (DatabaseError, InvalidRequestError) as db_error:
        handler = db_error_handling.get(  # type: ignore[call-overload]
            db_error.__class__,
            DBErrorHandling(
                http_status=http_status.HTTP_422_UNPROCESSABLE_ENTITY,
                msg=f"Could not delete  record for {model_cls} {db_error}",
            ),
        )
        logger.exception(handler.msg)
        db_session.rollback()
        return JSONResponse(
            status_code=handler.http_status,
            content={"detail": handler.msg},
        )
    return db_record  # type: ignore[no-any-return]


def get(
    model_cls: PartSnapBaseModel,
    db_session: Session,
    logger: Logger,
    query_statement: Any | None,
    db_error_handling: dict[DatabaseError, DBErrorHandling],
    list_wanted: bool = False,
) -> PartSnapBaseModel | JSONResponse | list[PartSnapBaseModel] | Any:
    """Retrieves one or all records from the database.

    If query_statement is None, this will query all objects in the database.
    Otherwise, it will execute the query statement to obtain the object id.

    FIXME: We will need to handle database pagination in the future as we may
    have a lot of records.

    Parameters
    ----------
    db_session: A valid database session
    logger: Logger instance to use to log information
    query_statement: An optional query statement to resolve the record id
    db_error_handling: Dictionary of error handling
    list_wanted: Returns a list even though a query statement is provided

    Returns
    -------

    PartSnapBaseModel: A single record if the query statement was for a single object.
    list[PartSnapBaseModel]: If all objects are queried
    JSONResponse: A object containing the error

    """

    table_name = model_cls.__class__.__name__
    if query_statement is not None:
        logger.debug(f"Getting single record from {table_name}")
        try:
            if list_wanted:
                db_records = db_session.exec(query_statement).all()
                # Handle cases where only one record is found but wrapped in a list
                if len(db_records) == 1:
                    # Makes sure to not return the list since there is only one record object
                    return db_records[0]
                # Return the list of records
                return db_records
            else:
                db_record = db_session.exec(query_statement).one()
                return db_record
        except (DatabaseError, InvalidRequestError) as db_error:
            handler = db_error_handling.get(  # type: ignore[call-overload]
                db_error.__class__,
                DBErrorHandling(
                    http_status=http_status.HTTP_404_NOT_FOUND,
                    msg=f"Failed to locate record in {table_name} - no mapping provided error",
                ),
            )
            # logger.exception(handler.msg)
            return JSONResponse(
                status_code=handler.http_status,
                content={"detail": handler.msg},
            )

    logger.debug(f"Getting all records from {table_name}")
    response = db_session.exec(select(model_cls)).all()  # type: ignore[call-overload]
    logger.debug(f"response {response}")
    return response


def get_list(
    model_cls: PartSnapBaseModel,
    db_session: Session,
    logger: Logger,
    query_statement: Any | None,
    db_error_handling: dict[DatabaseError, DBErrorHandling],
) -> list[PartSnapBaseModel] | JSONResponse:
    """Retrieves list of records from the database."""
    table_name = model_cls.__class__.__name__
    if query_statement is not None:
        logger.debug(f"Getting records from {table_name}")
        try:
            db_records = db_session.exec(query_statement).all()
        except (DatabaseError, InvalidRequestError) as db_error:
            handler = db_error_handling.get(  # type: ignore[call-overload]
                db_error.__class__,
                DBErrorHandling(
                    http_status=http_status.HTTP_404_NOT_FOUND,
                    msg=f"Failed to locate record(s) in {table_name} - no mapping provided error",
                ),
            )
            return JSONResponse(
                status_code=handler.http_status,
                content={"detail": handler.msg},
            )
        return db_records  # type: ignore[no-any-return]
    else:
        logger.debug(f"Getting all records from {table_name}")
        db_records = db_session.exec(select(model_cls)).all()  # type: ignore[call-overload]
        logger.debug(f"DB records = {db_records}")
        return db_records  # type: ignore[no-any-return]
