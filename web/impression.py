import json


class Impression(object):
    """
    Class designed to model all of the important information
    """
    def __init__(self, referer, domain):
        self._referer = referer
        self._domain = domain

    def __hash__(self):
        return hash((self._referer, self._domain))

    def __eq__(self, other):
        return self._referer == other._referer and self._domain == other._domain

    def domain(self):
        return self._domain

    def referer(self):
        return self._referer


def create_impression_from_json(impression_string):
    """
    Function to turn a string in to a Impression object

    :param impression_string: `string` string representation of an impression
    :return: `Impression`
    """

    impression_json = json.loads(impression_string)

    headers = impression_json['headers']

    referer = headers.get('Referer')
    domain = impression_json.get('page_domain')

    impression = Impression(referer, domain)
    return impression
