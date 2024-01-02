import requests
from bs4 import BeautifulSoup


class ChuckNorrisScraper:
    def __init__(self, scrape_api_key):
        self.url = 'https://parade.com/968666/parade/chuck-norris-jokes/'
        self.scrape_api_key = scrape_api_key
        self.jokes_ls = []

    def get_chuck_norris_jokes(self):
        response = requests.get(
            url='https://proxy.scrapeops.io/v1/',
            params={
                'api_key': self.scrape_api_key,
                'url': self.url,
            }
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the <ol> element with the jokes
        jokes_list = soup.find('ol')
        # Extract the text content of the <li> elements within the <ol>
        jokes = [li.get_text(strip=True) for li in jokes_list.find_all('li')]
        return jokes

    def set_jokes_list(self):
        self.jokes_ls = self.get_chuck_norris_jokes()
