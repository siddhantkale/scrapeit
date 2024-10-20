import requests
from bs4 import BeautifulSoup


class Amazon:
    url = "https://amazon.in/s"
    headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"
               }
    params = {}

    def __init__(self, user_search):
        self.params = {'k': user_search}

    def get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        while response.status_code == 503:
            response = requests.get(self.url, headers=self.headers, params=self.params)
        return response

    def get_product_images(self, soup):
        all_search_result = soup.find_all("div", class_="sg-col-inner")
        images_link = [
            a.find("img",class_="s-image") for a in all_search_result
        ]
        images_link = [
            a["src"] for a in images_link if a!=None
        ]
        return images_link

    def get_product_prices(self, soup):
        all_search_result = soup.find_all("div", class_="sg-col-inner")
        product_prices = [
            a.find("span",class_="a-price-whole") for a in all_search_result
        ]
        product_prices = ['₹' + a.text for a in product_prices if a!=None]

        return product_prices

    def get_product_names(self,soup):
        all_search_result = soup.find_all("div", class_="sg-col-inner")
        product_names = [
            a.find("span",class_="a-size-medium") for a in all_search_result
        ]
        product_names = [a.text for a in product_names if a!=None]
        return product_names

    def get_product_page(self, soup):
        all_search_result = soup.find_all("div", class_="sg-col-inner")
        product_page_link = [
            a.find("a", class_="a-link-normal s-no-outline") for a in all_search_result
            ]
        product_page_link = ["https://amazon.in" + a["href"] for a in product_page_link if a != None]
        return product_page_link

    def map_images(self):
        response = self.get_response();
        soup = BeautifulSoup(response.text, 'html.parser')
        images_link = self.get_product_images(soup)
        product_page_link = self.get_product_page(soup)
        product_page_prices = self.get_product_prices(soup)
        product_names = self.get_product_names(soup)
        image_product_page = []
        l = min(len(product_names), len(images_link), len(product_page_link), len(product_page_prices))
        for i in range(l):

            image_product_page.append(
                {
                    "product_link": product_page_link[i],
                    "image_link": images_link[i],
                    "product_price": product_page_prices[i],
                    "product_name": product_names[i],
                    "site": "Amazon"
                }
            )
        return image_product_page
