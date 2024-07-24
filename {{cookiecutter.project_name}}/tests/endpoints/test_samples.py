""" Simple tests sample endpoints.

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import pytest
from fastapi import status
from pydantic import ValidationError
from pytest_check import check

from {{cookiecutter.project_slug}}.model.sample import (
    SampleAPIModelCreate,
    SampleAPIModelRead,
    SampleAPIModelUpdate,
    SampleDBModel
)

create_args = {
    "word_string": "Hello partsnap",
    "description": "this is a partsnap string",
}
edit_args = {"word_string": "Hello test", "description": "this is a test"}


@pytest.fixture()
def a_sample(db_session):
    """Create and delete a sample"""
    new_sample = SampleAPIModelCreate(**create_args)

    sample = SampleDBModel.create(db_session=db_session, sample_model=new_sample)
    yield sample
    SampleDBModel.delete(db_session=db_session, sample_id=sample.id)


def test_get_all_samples(client, a_sample):
    response = client.get("/samples")
    with check:
        assert response.status_code == status.HTTP_200_OK
    with check:
        assert len(response.json()) >= 1
    assert a_sample in [SampleAPIModelRead(**json_wh) for json_wh in response.json()]


def test_get_sample_by_id(client, a_sample):
    resp_by_id = client.get(f"/samples/{a_sample.id}")
    with check:
        assert resp_by_id.status_code == status.HTTP_200_OK
    by_id = SampleAPIModelRead(**resp_by_id.json())
    with check:
        assert by_id == a_sample


def test_get_sample_by_word_string(client, a_sample):
    resp_by_word_string = client.get(f"/samples/{a_sample.word_string}")
    with check:
        assert resp_by_word_string.status_code == status.HTTP_200_OK
    by_word_string = SampleAPIModelRead(**resp_by_word_string.json())
    with check:
        assert by_word_string == a_sample


@pytest.mark.parametrize("word_string,description", [("foo goof", "goofy"), ("test lol", "haha test")])
def test_create_samples(client, word_string, description):
    new_sample = SampleAPIModelCreate(word_string=word_string, description=description)

    response = client.post("/samples/", json=new_sample.model_dump())
    resp_sample = SampleAPIModelCreate(**response.json())
    with check:
        assert response.status_code == status.HTTP_201_CREATED
    assert (
        SampleAPIModelCreate(**resp_sample.model_dump(exclude=["created_by", "updated_by"])) == new_sample
    )


def test_samples_put(client):
    print("Adding a Sample")
    sample = SampleAPIModelCreate(**create_args)
    response = client.post("/samples/", json=sample.model_dump())
    create_result = response.json()
    print(f"create_result = {create_result}")

    print("Editing a Sample")
    edit_sample = SampleAPIModelUpdate(**edit_args)
    response = client.put(f"/samples/{create_result['id']}", json=edit_sample.model_dump())
    assert response.status_code == status.HTTP_200_OK
    edit_result = response.json()
    for k in edit_args:
        assert edit_args[k] == edit_result[k]

    print("Get edited Sample")
    response = client.get(f"/samples/{create_result['id']}")
    get_result = response.json()
    for k in edit_args:
        assert edit_args[k] == get_result[k]


@pytest.mark.parametrize("word_string,description", [(None, "will I work")])
def test_create_sample_word_string_none(word_string, description):
    print("Check that the sample can't be created with None type")
    with pytest.raises(ValidationError):
        SampleAPIModelCreate(word_string=word_string, description=description)


def test_delete_sample(client, a_sample):
    response = client.delete(f"/samples/{a_sample.id}")
    assert response.status_code == status.HTTP_200_OK
    response = client.get(f"/samples/{a_sample.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
