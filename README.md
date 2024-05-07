# Web Crawler Email

This is a Python script for extracting email addresses from websites and recursively crawling them up to a specified depth.

## Features

- Extracts email addresses from web pages using regular expressions.
- Respects `robots.txt` directives to avoid crawling disallowed pages.
- Supports command-line arguments for specifying URLs and crawling depth.
- Logs crawling activity and extracted email addresses to a file for analysis.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/web-crawler.git
    ```

2. **Install Requirements:**
    ```bash
    pip install -r requests beautifulsoup4
    ```

3. **Run the Script:**
    ```bash
    python crawl_email.py https://example.com -d 2
    ```
    Replace `https://example.com` with the URL you want to crawl, and `-d 2` with the desired depth.

## Command-line Arguments

- `urls`: URLs of the websites to crawl.
- `-d`, `--depth`: Depth of crawling (default: 1).
- `-t`, `--timeout`: Timeout for HTTP requests in seconds (default: 10).

## Logging

Crawling activity and extracted email addresses are logged to `crawler.log`.

## Acknowledgements

- This script uses the following libraries:
    - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
    - [Requests](https://docs.python-requests.org/en/latest/)
    - [Urllib](https://docs.python.org/3/library/urllib.html)

