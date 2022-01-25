# This program takes a website and scrapes it for the text in h3 elements,
# It is currently writen to grab the headlines from bbc.com and output them into a text file
import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # request a website's html data, store in r variable
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        # for each anchor tag on the page
        with open("headlines.txt", "w") as file:
            # Find the h3 tags and grab their text, output it to the headlines file
            for tag in sp.find("body").find_all("h3"):
                file.write(tag.text.strip() + "\n")


news = "https://www.bbc.com/news"
Scraper(news).scrape()
