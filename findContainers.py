from lxml import html
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = "https://www.flighthub.com/flight/search?num_segments=1&seg0_date=2017-10-09&seg0_time=&seg0_from=SFO&seg0_to=LAX&num_adults=1&num_children=0&seat_class=Economy&campaign=4402&flexible_date=1&search_id=d1adc7ddf34b55353d4cbe562affcb9d&flexible_search_id=f59dc438a178da9a6fa119d4a4a908cb"
page_client = urlopen(url)
page_html = page_client.read()
page_client.close()
page_soup = soup(page_html, "html.parser")

flights = page_soup.find_all("div", {"class" : "packages-os-wrap"})

prices = page_soup.find_all("div", {"class" : "packages-os-top"})

print(len(flights))