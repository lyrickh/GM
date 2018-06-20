import pytest
from web.impression import create_impression_from_json


def test_create_impression():
    impression_json = {"page_domain": "domain", "headers": {"Referer": "referer"}}
    impression = create_impression_from_json(impression_json)

    assert impression.domain() == "domain"
    assert impression.referer() == "referer"


def test_create_impression_assigns_defaults():
    impression_json = {"not_used": "hello", "headers": {}}
    impression = create_impression_from_json(impression_json)

    assert impression.domain() is None
    assert impression.referer() is None


def test_json_without_header_fails():
    impression_json = {"not_used": "hello"}

    with pytest.raises(KeyError):
        create_impression_from_json(impression_json)
