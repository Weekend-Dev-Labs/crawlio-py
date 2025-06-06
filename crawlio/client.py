import requests
from typing import Optional, Dict, Any

from .exception import (
    CrawlioAuthenticationError,
    CrawlioError,
    CrawlioFailureError,
    CrawlioInternalServerError,
    CrawlioLimitExceeded,
    CrawlioRateLimit
)

from .types import (
    ScrapeOptions,
    CrawlOptions,
    SearchOptions,
    BatchScrapeOptions,
    ScrapeResponse,
    CrawlResponse,
    CrawlStatusResponse,
    CrawlResultResponse,
    SearchResponse,
    BatchScrapeResponse,
    BatchScrapeStatusResponse,
    BatchScrapeResultResponse
)


class Crawlio:
    def __init__(self, api_key: str, base_url: str = "https://crawlio.xyz"):
        if not api_key:
            raise CrawlioError("apiKey is required to initialize Crawlio client.")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, endpoint: str, data: Optional[dict] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.request(method, url, json=data, headers=headers)
        try:
            body = response.json()
        except ValueError:
            raise CrawlioError("Invalid JSON response", {"status_code": response.status_code})

        self._handle_status(response.status_code, body)
        return body

    def _handle_status(self, status: int, body: dict) -> None:
        if status == 429:
            raise CrawlioRateLimit("Rate limit exceeded", body)
        elif status == 403:
            raise CrawlioAuthenticationError("Authentication failed", body)
        elif status == 500:
            raise CrawlioInternalServerError("Server error", body)
        elif status >= 400:
            raise CrawlioFailureError(f"Request failed with status {status}", body)

    def scrape(self, options: ScrapeOptions) -> ScrapeResponse:
        return self._request("POST", "/api/scrape", options)

    def crawl(self, options: CrawlOptions) -> CrawlResponse:
        return self._request("POST", "/api/crawl", options)

    def crawl_status(self, crawl_id: str) -> CrawlStatusResponse:
        return self._request("GET", f"/api/crawl/status/{crawl_id}")

    def crawl_results(self, crawl_id: str) -> CrawlResultResponse:
        return self._request("GET", f"/api/crawl/{crawl_id}")

    def search(self, query: str, options: Optional[SearchOptions] = None) -> SearchResponse:
        payload: Dict[str, Any] = {"query": query}
        if options:
            payload.update(options)
        return self._request("POST", "/api/results", payload)

    def batch_scrape(self, options: BatchScrapeOptions) -> BatchScrapeResponse:
        return self._request("POST", "/api/scrape/batch", options)

    def batch_scrape_status(self, batch_id: str) -> BatchScrapeStatusResponse:
        return self._request("GET", f"/api/scrape/batch/status/{batch_id}")

    def batch_scrape_result(self, batch_id: str) -> BatchScrapeResultResponse:
        return self._request("GET", f"/api/scrape/batch/{batch_id}")
