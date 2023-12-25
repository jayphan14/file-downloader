import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(url, folder_path="."):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder_path, url.split("/")[-1])
        with open(filename, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"Downloaded: {filename}")

def download_pdfs_from_webpage(webpage_url, folder_path="."):
    response = requests.get(webpage_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all anchor tags with href attribute
        for link in soup.find_all('a', href=True):
            href = link['href']
            pdf_url = urljoin(webpage_url, href)
            download_pdf(pdf_url, folder_path)

def main():
    # Check if at least one URL is provided
    if len(sys.argv) < 2:
        print("Usage: pdf_downloader <URL1> [URL2 ...]")
        sys.exit(1)

    # Extract URLs from command-line arguments
    urls = sys.argv[1]

    # Download PDFs from each URL to the specified folder
    for url in urls:
        download_pdfs_from_webpage(url)

if __name__ == "__main__":
    main()

