from mock import sentinel
from web.impression import Impression
import web.db


def test_add_impressions(setup_db):
    impression = Impression(sentinel.referer, sentinel.domain)
    web.db.add_impression(impression)

    assert "Impressions" in web.db._FAKE_DB
    assert len(web.db._FAKE_DB["Impressions"]) == 1
    assert web.db._FAKE_DB["Impressions"] == [impression]

    impression2 = Impression(sentinel.referer2, sentinel.domain2)
    web.db.add_impression(impression2)

    assert len(web.db._FAKE_DB["Impressions"]) == 2
    assert web.db._FAKE_DB["Impressions"] == [impression, impression2]


def test_get_all_impressions(setup_db):
    impression = Impression(sentinel.referer, sentinel.domain)
    impression2 = Impression(sentinel.referer2, sentinel.domain2)

    web.db._FAKE_DB = {"Impressions": [impression, impression2]}

    assert web.db.get_all_impressions() == [impression, impression2]


def test_no_impressions_returns_empty_list(setup_db):
    assert web.db.get_all_impressions() == []
