import json
import re
import sys
from urllib.request import urlopen, Request
try:
    from packaging.version import Version
except (ModuleNotFoundError, ImportError):
    from distutils.version import LooseVersion as Version

element_pat = re.compile(r'<(.+?)>')
rel_pat = re.compile(r'rel=[\'"](\w+)[\'"]')


def fetch_url(url):
    req = Request(url)
    try:
        print("fetching %s" % url, file=sys.stderr)
        f = urlopen(req)
    except Exception as e:
        print(e)
        print("return Empty data", file=sys.stderr)
        return {}

    return f


def parse_link_header(headers):
    link_s = headers.get('link', '')
    urls = element_pat.findall(link_s)
    rels = rel_pat.findall(link_s)
    d = {}
    for rel, url in zip(rels, urls):
        d[rel] = url
    return d


def get_json_from_url(url):
    """Fetch and read url."""
    f = fetch_url(url)
    return json.load(f) if f else {}


def get_paged_request(url):
    """Get a full list, handling APIv3's paging."""
    results = []
    while url:
        f = fetch_url(url)
        if not f:
            continue
        results.extend(json.load(f))
        links = parse_link_header(f.headers)
        url = links.get('next')
    return results


def get_tags(project="dipy/dipy", min_version="1.1.1"):
    """Get a list of the tags from the Github API."""
    url = "https://api.github.com/repos/{0}/tags".format(project)
    tags = get_paged_request(url)
    return [t.get("name") for t in tags
            if not t.get("name").lower().islower()
            if Version(t.get("name")) >= Version(min_version)]



print('pre hooks')
