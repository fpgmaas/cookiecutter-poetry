""" Sample routes

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import json
from typing import Annotated

import sqlalchemy
from fastapi import APIRouter, Depends, Query
from fastapi import status as http_status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import Union

from {{cookiecutter.project_slug}}.dependencies import ps_db_session
from {{cookiecutter.project_slug}}.logging import psnap_get_logger
from {{cookiecutter.project_slug}}.model.sample import SampleAPIModelCreate, SampleAPIModelRead, SampleAPIModelUpdate, SampleDBModel
from {{cookiecutter.project_slug}}.routers.api_models import ErrorMessageModel

router = APIRouter(prefix="/samples", tags=["samples"])
LOGGER = psnap_get_logger("router.samples")


def can_convert_to_int(value):
    """Check if a value can be converted to an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False


@router.get("/", response_model=list[SampleAPIModelRead])
async def get_samples(
    db_engine: Annotated[sqlalchemy.Engine, Depends(ps_db_session)],
) -> list[SampleAPIModelRead]:
    LOGGER.info("GET /samples/")
    with Session(db_engine) as db_session:
        return SampleDBModel.get(db_session=db_session)  # type: ignore[return-value]


@router.get("/{sample_data}", response_model=Union[list[SampleAPIModelRead], SampleAPIModelRead])
async def get_sample(
    sample_data: int | str,
    db_engine: Annotated[sqlalchemy.Engine, Depends(ps_db_session)],
) -> SampleAPIModelRead | list[SampleAPIModelRead] | JSONResponse:
    LOGGER.info(f"GET /samples/{sample_data}")
    # Validate input
    if can_convert_to_int(sample_data):
        # Convert sample_id to an integer
        sample_id = sample_data
        # Fetch by sample_id
        with Session(db_engine) as db_session:
            return SampleDBModel.get(db_session=db_session, sample_id=sample_id)  # type: ignore[return-value]
    else:
        word_string = sample_data
        # Fetch by word_string
        with Session(db_engine) as db_session:
            return SampleDBModel.get(db_session=db_session, word_string=word_string)  # type: ignore[return-value]

@router.post(
    "/",
    response_model=SampleAPIModelRead,
    status_code=http_status.HTTP_201_CREATED,
    responses={
        http_status.HTTP_201_CREATED: {"model": SampleAPIModelRead},
        http_status.HTTP_409_CONFLICT: {"model": ErrorMessageModel},
    },
)
async def create_sample(
    sample_data: SampleAPIModelCreate,
    db_engine: Annotated[sqlalchemy.Engine, Depends(ps_db_session)],
) -> SampleAPIModelRead | JSONResponse:
    LOGGER.info(f"POST /samples/ data={sample_data.model_dump()}")

    LOGGER.info("with Session(db_engine) as db_session:")
    with Session(db_engine) as db_session:
        response = SampleDBModel.create(db_session=db_session, sample_model=sample_data)
        if isinstance(response, SampleAPIModelRead):
            LOGGER.debug(f"POST [OK]  /samples/ data={json.dumps(response.model_dump(), indent=2)}")
        if isinstance(response, JSONResponse):
            LOGGER.error(
                f"POST [FAILED]  /samples/ data={sample_data} response {response.status_code} {response.body.decode('utf-8')}"
            )
        return response  # type: ignore[return-value]


@router.put(
    "/{sample_id}",
    response_model=SampleAPIModelRead,
    status_code=http_status.HTTP_200_OK,
    responses={
        http_status.HTTP_200_OK: {"model": SampleAPIModelRead},
        http_status.HTTP_406_NOT_ACCEPTABLE: {"model": ErrorMessageModel},
    },
)
async def update_sample(
    sample_data: SampleAPIModelUpdate,
    sample_id: int | str,
    db_engine: Annotated[sqlalchemy.Engine, Depends(ps_db_session)],
) -> SampleAPIModelCreate | JSONResponse:
    LOGGER.info(f"PUT /samples/{sample_id} data={sample_data.model_dump()}")

    with Session(db_engine) as db_session:
        response = SampleDBModel.update(db_session=db_session, sample_id=sample_id, sample_model=sample_data)
        if isinstance(response, SampleAPIModelRead):
            LOGGER.debug(f"PUT [OK]  /samples/{sample_id} data={json.dumps(response.model_dump(), indent=2)}")
        if isinstance(response, JSONResponse):
            LOGGER.error(
                f"PUT [FAILED]  /samples/{sample_id} data={sample_data} response {response.status_code} {response.body.decode('utf-8')}"
            )
        return response  # type: ignore[return-value]


@router.delete(
    "/{sample_id}",
    status_code=http_status.HTTP_200_OK,
    response_model=SampleAPIModelRead,
    responses={
        http_status.HTTP_200_OK: {"model": SampleAPIModelRead},
        http_status.HTTP_404_NOT_FOUND: {"model": ErrorMessageModel},
    },
)
async def delete_sample(
    sample_id: int | str,
    db_engine: Annotated[sqlalchemy.Engine, Depends(ps_db_session)],
) -> SampleAPIModelRead | JSONResponse:
    LOGGER.info(f"DELETE /samples/{sample_id}")

    with Session(db_engine) as db_session:
        response = SampleDBModel.delete(db_session=db_session, sample_id=sample_id)
        if isinstance(response, SampleAPIModelRead):
            LOGGER.debug(
                f"DELETE [OK]  /samples/{sample_id} response {json.dumps(response.model_dump(), indent=2)}"
            )
        if isinstance(response, JSONResponse):
            LOGGER.error(
                f"DELETE [FAILED]  /samples/{sample_id} response {response.status_code} {response.body.decode('utf-8')}"
            )
        return response
