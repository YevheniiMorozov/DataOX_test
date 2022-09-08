import re
import time
import datetime
import requests
from bs4 import BeautifulSoup


def get_data():
    page = 1
    cards = []
    while True:
        url = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36",
        }
        r = requests.get(url=url, headers=headers)
        time.sleep(3)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.text, 'lxml')
        if page > 1:
            check_page = soup.find("title").text.strip()[-10:]
            if int(re.findall(r"\d+", check_page)[0]) != page:
                break
        list_apartments = soup.find_all('div', class_="search-item")
        for element in list_apartments:
            element_dict = {"apartments": {
                "url": "https://www.kijiji.ca" + element.get("data-vip-url"),
                "img_src": element.find("img").get("data-src"),
                "city": element.find('div', {'class': "location"}).find("span").text.strip(),
                "time": element.find('div', {'class': "location"}).find("span", {"class": "date-posted"}).text.strip(),
                "description": element.find('div', {'class': "description"}).text.strip().replace("\n", ' '),
                'bedrooms': "".join(element.find(
                    "div", {'class': "rental-info"}
                                         ).find("span", {"class": "bedrooms"}).text.strip().split()),
                },
                "price": element.find('div', {"class": "price"}).text.strip()
            }
            if element_dict['apartments']["time"].startswith("<"):
                element_dict['apartments']["time"] = datetime.date.today().strftime("%d-%m-%Y")
            elif element_dict['apartments']["time"] == "Yesterday":
                element_dict['apartments']["time"] = (
                        datetime.date.today() - datetime.timedelta(days=1)
                ).strftime("%d-%m-%Y")
            else:
                element_dict['apartments']["time"] = element_dict['apartments']["time"].replace("/", "-")
            cards.append(element_dict)
        print(f"Info from page {page} added")
        page += 1
    return cards
