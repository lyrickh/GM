_FAKE_DB = dict()


def add_impression(impression):
    """
    Add an impression in to the db

    :param impression: `Impression` the impression to be stored
    :return:
    """
    global _FAKE_DB
    _FAKE_DB.setdefault("Impressions", []).append(impression)


def get_all_impressions():
    """
    Gets all of the impressions currently stored in the database

    :return: `list` A list of all the impressions stored in the dv
    """
    global _FAKE_DB
    return _FAKE_DB.get("Impressions", [])
