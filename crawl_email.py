import argparse
import requests
from bs4 import BeautifulSoup
import re
import logging
import urllib.robotparser
import time

def setup_logger():
    logging.basicConfig(filename='crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def extract_emails(url):
    # Send a GET request to the URL
    response = requests.get(url, timeout=10)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all email addresses using a regular expression
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())
        
        # Remove duplicates
        unique_emails = list(set(emails))
        
        return unique_emails
    else:
        logging.warning(f"Failed to retrieve page: {response.status_code} - {url}")
        return []

def crawl(url, depth, visited, max_depth):
    if depth > max_depth:
        return
    
    visited.add(url)
    logging.info(f"Crawling: {url}")
    
    # Check robots.txt compliance
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{url}/robots.txt")
    rp.read()
    if not rp.can_fetch("*", url):
        logging.warning(f"Robots.txt disallows crawling: {url}")
        return
    
    # Extract emails
    emails = extract_emails(url)
    
    # Log extracted emails
    for email in emails:
        logging.info(f"Email found: {email}")
    
    # Find links on the page and recursively crawl them
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = link['href']
            if next_url.startswith('http') and next_url not in visited:
                crawl(next_url, depth + 1, visited, max_depth)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract email addresses from websites and crawl them.")
    parser.add_argument("urls", nargs='+', type=str, help="URLs of the websites to crawl")
    parser.add_argument("-d", "--depth", type=int, default=1, help="Depth of crawling (default: 1)")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Timeout for HTTP requests in seconds (default: 10)")
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Set up logging
    setup_logger()
    
    # Crawl each URL
    for url in args.urls:
        crawl(url, 1, set(), args.depth)

if _name_ == "_main_":
    print("Created by ALIEN0X")
    main()
