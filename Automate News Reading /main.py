import requests
from bs4 import BeautifulSoup
import redis
import datetime


class Scraper():

    def __init__(self, keywords):
        self.markup = requests.get("https://news.ycombinator.com/").text
        self.keywords = keywords

    def parse(self):
        soup = BeautifulSoup(self.markup, "html.parser")
        links = soup.findAll("a", {"class": "storylink"})

        self.saved_links = []

        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.saved_links.append(link)

    def store(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        for link in self.saved_links:
            r.set(link.text, str(link))

    def email(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        links = [r.get(k) for k in r.keys()]
        print(links)

        r.flushdb()


s = Scraper(['data science', 'machine learning',
             'machines', 'Covid-19', 'novel'])
s.parse()
s.store()
if datetime.time.hour == 13:
    s.email()
