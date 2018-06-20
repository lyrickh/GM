from mock import sentinel
from web.impression import Impression
from web.db import add_impression, get_all_impressions, _FAKE_DB


def test_add_impressions(setup_db):
    assert _FAKE_DB == dict()

    impression = Impression(sentinel.referer, sentinel.domain)
    add_impression(impression)

    assert "Impressions" in _FAKE_DB
    assert len(_FAKE_DB["Impressions"]) == 1
    assert _FAKE_DB["Impressions"] == [impression]

    impression2 = Impression(sentinel.referer2, sentinel.domain2)
    add_impression(impression2)

    assert len(_FAKE_DB["Impressions"]) == 2
    assert _FAKE_DB["Impressions"] == [impression, impression2]


def test_get_all_impressions(setup_db):
    assert _FAKE_DB == dict()

    impression = Impression(sentinel.referer, sentinel.domain)
    add_impression(impression)

    impression2 = Impression(sentinel.referer2, sentinel.domain2)
    add_impression(impression2)

    assert get_all_impressions() == [impression, impression2]
