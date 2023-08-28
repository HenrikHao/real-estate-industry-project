import re
import time
from json import dump
from collections import defaultdict
from bs4 import BeautifulSoup
import requests

# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 2)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
}

url_links = []
property_metadata = defaultdict(dict)

def make_request(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=60)
        return BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print(f"Error while fetching {url}. Error: {e}")
        return None

for page in N_PAGES:
    url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    print(f"Visiting {url}")
    
    bs_object = make_request(url)
    if not bs_object:
        continue

    index_links = bs_object \
        .find("ul", {"data-testid": "results"}) \
        .findAll("a", href=re.compile(f"{BASE_URL}/*"))

    for link in index_links:
        if 'address' in link['class']:
            url_links.append(link['href'])

    time.sleep(5)  # Sleep for 5 seconds between page requests to avoid rate limits

for property_url in url_links[1:]:
    bs_object = make_request(property_url)
    if not bs_object:
        continue

    try: 
        property_metadata[property_url]['name'] = bs_object \
            .find("h1", {"class": "css-164r41r"}) \
            .text

        property_metadata[property_url]['cost_text'] = bs_object \
            .find("div", {"data-testid": "listing-details__summary-title"}) \
            .text

        property_metadata[property_url]['coordinates'] = [
            float(coord) for coord in re.findall(
                r'destination=([-\s,\d\.]+)',
                bs_object \
                    .find(
                        "a",
                        {"target": "_blank", 'rel': "noopener noreferer"}
                    ) \
                    .attrs['href']
            )[0].split(',')
        ]

        '''rooms = bs_object \
                .find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"})

        property_metadata[property_url]['rooms'] = [
            re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Bed' in feature.text or 'Bath' in feature.text
        ]'''
        rooms_list = []
        for feature in bs_object \
                .find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"}):
            try:
                rooms_list.append(re.findall(r'\d\s[A-Za-z]+', feature.text)[0])
            except IndexError:
                pass
        property_metadata[property_url]['rooms'] = rooms_list
        '''property_metadata[property_url]['parking'] = [
            re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Parking' in feature.text
        ]'''

        property_metadata[property_url]['desc'] = bs_object.find("p").text

    except AttributeError:
        print(f"Issue with {property_url}, see raw dump below")
        print(bs_object.text)
        continue

    time.sleep(5)  # Sleep for 5 seconds between individual property requests

with open('../data/raw/example.json', 'w') as f:
    dump(property_metadata, f)
