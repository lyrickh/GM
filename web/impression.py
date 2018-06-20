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
