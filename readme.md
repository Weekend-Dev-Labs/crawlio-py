# 🕷️ Crawlio Python SDK

**Crawlio** is a Python SDK for accessing the Crawlio API — a powerful service for web scraping, crawling, and content analysis. It supports single-page scraping, full site crawling, batch operations, and structured search across results.

---

## 📦 Installation

```bash
pip install crawlio-py
```

---

## 🚀 Getting Started

```python
from crawlio.client import Crawlio

client = Crawlio(api_key="your-api-key")

result = client.scrape({
    "url": "https://example.com",
    "markdown": True
})

print(result["markdown"])
```

---

## 🔐 Authentication

You must pass your Crawlio `api_key` when instantiating the client.

```python
client = Crawlio(api_key="your_api_key")
```

---

## 🧭 Usage

### `scrape(options: dict) -> dict`

Scrape a single webpage.

```python
client.scrape({
    "url": "https://example.com",
    "exclude": ["nav", "footer"],
    "markdown": True
})
```

---

### `crawl(options: dict) -> dict`

Start a full-site crawl.

```python
client.crawl({
    "url": "https://example.com",
    "count": 10,
    "sameSite": True
})
```

---

### `crawl_status(crawl_id: str) -> dict`

Check the status of a crawl job.

```python
client.crawl_status("crawl123")
```

---

### `crawl_results(crawl_id: str) -> dict`

Get results from a completed crawl.

```python
client.crawl_results("crawl123")
```

---

### `search(query: str, options: dict = None) -> dict`

Search through previously scraped content.

```python
client.search("privacy policy", {"site": "example.com"})
```

---

### `batch_scrape(options: dict) -> dict`

Submit multiple URLs for scraping at once.

```python
client.batch_scrape({
    "url": ["https://a.com", "https://b.com"],
    "options": {"markdown": True}
})
```

---

### `batch_scrape_status(batch_id: str) -> dict`

Check the status of a batch scrape.

```python
client.batch_scrape_status("batch456")
```

---

### `batch_scrape_result(batch_id: str) -> dict`

Retrieve results of a completed batch scrape.

```python
client.batch_scrape_result("batch456")
```

---

## 🧨 Error Handling

All exceptions inherit from `CrawlioError`.

### Exception Types

| Exception Class              | Description                    |
| ---------------------------- | ------------------------------ |
| `CrawlioError`               | Base error class               |
| `CrawlioRateLimit`           | Too many requests              |
| `CrawlioLimitExceeded`       | API usage limit exceeded       |
| `CrawlioAuthenticationError` | Invalid or missing API key     |
| `CrawlioInternalServerError` | Server error                   |
| `CrawlioFailureError`        | Other client or server failure |

Example:

```python
try:
    result = client.scrape({"url": "https://example.com"})
except CrawlioError as e:
    print(f"Error: {e}, Details: {e.response}")
```

---

## 📄 Response Format (Example)

### `Scrape`

```json
{
  "jobId": "abc123",
  "html": "<html>...</html>",
  "markdown": "## Title",
  "meta": {"title": "Example"},
  "urls": ["https://example.com/about"],
  "url": "https://example.com"
}
```

---

## 📃 License

MIT License

---