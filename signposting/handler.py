"""
"""

from pywb.webapp.handlers import WBHandler
from pywb.webapp.live_rewrite_handler import RewriteHandler

__author__ = 'Harihar Shankar'


class SignpostingHandler(WBHandler):

    def __init__(self, config):
        super(SignpostingHandler, self).__init__(config)

    def handle_request(self, wbrequest):
        return self.index_reader.make_cdx_response(wbrequest, None, None)


class SignpostingRewriteHandler(RewriteHandler):
    def __init__(self, config):
        super(SignpostingRewriteHandler, self).__init__(config)

        self.templates = config.get("templates", {})

    @staticmethod
    def get(key):
        return None
