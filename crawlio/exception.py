from typing import Optional

class CrawlioError(Exception):
    def __init__(self, message: str, response: Optional[dict] = None):
        super().__init__(message)
        self.response = response or {}

class CrawlioRateLimit(CrawlioError): pass
class CrawlioLimitExceeded(CrawlioError): pass
class CrawlioAuthenticationError(CrawlioError): pass
class CrawlioInternalServerError(CrawlioError): pass
class CrawlioFailureError(CrawlioError): pass