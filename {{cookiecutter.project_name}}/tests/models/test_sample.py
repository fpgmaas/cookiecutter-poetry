""" Simple tests sample models.

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

from fastapi import status as http_status
from fastapi.responses import JSONResponse
from pytest_check import check

from {{cookiecutter.project_slug}}.model.sample import (
    SampleAPIModelCreate,
    SampleAPIModelRead,
    SampleAPIModelUpdate,
    SampleDBModel
)


def test_create_sample(db_session):
    sample = SampleAPIModelCreate(word_string="this is a test", description="a test")
    db_sample = SampleDBModel.create(db_session=db_session, sample_model=sample)
    with check:
        assert sample == SampleAPIModelCreate(
            **db_sample.model_dump(
                exclude=[
                    "created_by",
                    "updated_by",
                ]
            )
        )
    SampleDBModel.delete(db_session=db_session, sample_id=db_sample.id)


def test_get_sample(db_session, db_sample):
    db_sample_by_id = SampleDBModel.get(db_session=db_session, sample_id=db_sample.id)
    assert db_sample_by_id == db_sample
    db_sample_by_word_string = SampleDBModel.get(db_session=db_session, word_string=db_sample.word_string)
    assert db_sample_by_word_string == db_sample


def test_get_all_samples(db_session, db_sample):
    assert db_sample in SampleDBModel.get(db_session=db_session)


def test_get_sample_not_found(db_session):
    db_sample = SampleDBModel.get(db_session=db_session, sample_id="FKU")
    assert isinstance(db_sample, JSONResponse)
    assert db_sample.status_code == http_status.HTTP_404_NOT_FOUND
    db_sample = SampleDBModel.get(db_session=db_session, word_string="FKU")
    assert isinstance(db_sample, JSONResponse)
    assert db_sample.status_code == http_status.HTTP_404_NOT_FOUND


def test_update_sample(db_session, db_sample):
    edited_sample = SampleDBModel.update(
        db_session=db_session,
        sample_id=db_sample.id,
        sample_model=SampleAPIModelUpdate(word_string="Hi update", description="I have been updated"),
    )
    with check:
        assert isinstance(edited_sample, SampleAPIModelRead)
    with check:
        assert edited_sample.word_string == "Hi update"


def test_delete_sample(db_session, db_sample):
    response = SampleDBModel.delete(db_session=db_session, sample_id=db_sample.id)
    with check:
        assert isinstance(response, SampleAPIModelRead)
    with check:
        assert response == db_sample
    with check:
        print("Make sure that the record was indeed deleted")
        assert isinstance(SampleDBModel.get(db_session=db_session, sample_id=db_sample.id), JSONResponse)
