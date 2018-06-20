import pytest
import web.db


@pytest.fixture(scope="function")
def setup_db(request):
    web.db._FAKE_DB = dict()

    def teardown():
        web.db._FAKE_DB = dict()

    request.addfinalizer(teardown)

