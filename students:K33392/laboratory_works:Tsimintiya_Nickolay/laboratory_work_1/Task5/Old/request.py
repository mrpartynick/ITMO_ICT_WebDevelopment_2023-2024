from functools import lru_cache
from urllib.parse import parse_qs, urlparse

class Request:
  def __init__(self, method, target, version, rfile):
    self.method = method
    self.target = target
    self.version = version
    self.rfile = rfile

  @property
  def path(self):
    return self.url.path

  @property
  @lru_cache(maxsize=None)
  def query(self):
    return parse_qs(self.url.query)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)