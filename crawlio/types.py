from typing import TypedDict, Optional, List, Dict, Literal


CrawlStatus = Literal["IN_QUEUE", "RUNNING", "LIMIT_EXCEEDED", "ERROR", "SUCCESS"]
WorkflowType = Literal["scroll", "click", "wait", "eval", "screenshot"]


# Request Options
class Workflow(TypedDict, total=False):
    type: WorkflowType
    selector: Optional[str]
    script: Optional[str]
    duration: Optional[int]
    id: Optional[str]


class ScrapeOptions(TypedDict, total=False):
    url: str
    exclude: List[str]
    includeOnly: List[str]
    markdown: bool
    returnUrls: bool
    workflow: List[Workflow]
    normalizeBase64: bool


class CrawlOptions(TypedDict, total=False):
    url: str
    exclude: List[str]
    includeOnly: List[str]
    sameSite: bool
    count: int
    patterns: List[str]


class SearchOptions(TypedDict, total=False):
    site: str


class BatchScrapeOptions(TypedDict):
    url: List[str]
    options: ScrapeOptions


# Response Types
class EvaluationResult(TypedDict, total=False):
    result: str
    error: str


class ScrapeResponse(TypedDict, total=False):
    jobId: str
    html: str
    markdown: str
    meta: Dict[str, str]
    urls: List[str]
    url: str
    evaluation: Dict[str, EvaluationResult]
    screenshots: Dict[str, str]


class CrawlResponse(TypedDict):
    crawlId: str


class CrawlStatusResponse(TypedDict):
    id: str
    status: CrawlStatus
    error: int
    success: int
    total: int


class CrawlResultItem(TypedDict):
    id: str
    result: ScrapeResponse


class CrawlResultResponse(TypedDict, total=False):
    id: str
    results: List[CrawlResultItem]
    next: Optional[str]
    total: int


class SearchItem(TypedDict, total=False):
    title: str
    description: Optional[str]
    link: str


class SearchResponse(TypedDict):
    jobId: str
    results: List[SearchItem]


class BatchScrapeResponse(TypedDict):
    batchId: str


class BatchScrapeStatusResponse(TypedDict):
    id: str
    status: CrawlStatus
    error: int
    success: int


class BatchScrapeResultItem(TypedDict):
    id: str
    result: ScrapeResponse


class BatchScrapeResultResponse(TypedDict, total=False):
    id: str
    results: List[BatchScrapeResultItem]
    next: Optional[str]
    total: int
