from web.read_file_dump import create_impression_from_json


def test_create_impression():
    impression_string = '{"page_domain": "domain", "headers": {"Referer": "ref"}}'
    impression = create_impression_from_json(impression_string)

    assert impression.domain() == "domain"
    assert impression.referer() == "referer"


def test_create_impression_assigns_defaults():
    impression_string = '{"not_used": "hello"}'
    impression = create_impression_from_json(impression_string)

    assert impression.domain() is None
    assert impression.referer() is None
