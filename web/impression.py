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
        if type(self) != type(other):
            return False
        return self.referer() == other.referer() and self.domain() == other.domain()

    def domain(self):
        return self._domain

    def referer(self):
        return self._referer


def create_impression_from_json(impression_json):
    """
    Function to turn a string in to a Impression object

    :param impression_json: `dict` json representation of an impression
    :return: `Impression`
    """

    headers = impression_json['headers']

    referer = headers.get('Referer')
    domain = impression_json.get('page_domain')

    impression = Impression(referer, domain)
    return impression
