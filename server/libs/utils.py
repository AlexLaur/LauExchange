import urlparse

def get_params_from_url(url=None):
    parsed = urlparse.urlparse(url)
    params = urlparse.parse_qs(parsed.query)
    return params