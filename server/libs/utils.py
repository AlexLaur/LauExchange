try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

def get_params_from_url(url=None):
    parsed = urlparse.urlparse(url)
    params = urlparse.parse_qs(parsed.query)
    output = {}
    for key, value in params.items():
        if value:
            output[key] = value[0]
    return output