import requests
from bs4 import BeautifulSoup
class Flipkart:
    url = "https://www.flipkart.com/search"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    params = {}
    def __init__(self,user_search):
        self.params = {'q': user_search}

    def get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        while response.status_code == 503:
            response = requests.get(self.url, headers=self.headers, params=self.params)
        return response

    def get_product_images(self, soup):
        all_search_result = soup.find_all("div", class_="tUxRFH")
        product_images = [
            a.find("img",class_="DByuf4")["src"] for a in all_search_result
        ]
        return product_images



    def get_product_page(self, soup):

        all_search_result = soup.find_all("div",class_="tUxRFH")
        product_page_link = [
            a.find("a",class_="CGtC98") for a in all_search_result
        ]
        product_page_link = ["https://flipkart.com" + a["href"] for a in product_page_link]

        return product_page_link


    def get_product_names(self,soup):
        all_search_result = soup.find_all("div", class_="tUxRFH")
        product_names = [
            a.find("div", class_="KzDlHZ") for a in all_search_result
        ]
        product_names = [a.text for a in product_names if a!=None]
        return product_names


    def get_product_price(self,soup):
        all_search_result = soup.find_all("div", class_="tUxRFH")
        product_prices = [
            a.find("div",class_="Nx9bqj _4b5DiR") for a in all_search_result
        ]
        product_prices = [a.text for a in product_prices]
        return product_prices


    def map_images(self):
        response = self.get_response()
        soup = BeautifulSoup(response.text, 'html.parser')
        images_link = self.get_product_images(soup)
        product_page_link = self.get_product_page(soup)
        product_page_prices = self.get_product_price(soup)
        product_names = self.get_product_names(soup)
        image_product_page = []
        l = min(len(product_names),len(images_link),len(product_page_link),len(product_page_prices))
        for i in range(l):
            image_product_page.append(
                {
                    "product_link": product_page_link[i],
                    "image_link": images_link[i],
                    "product_price": product_page_prices[i],
                    "product_name" : product_names[i],
                    "site": "Flipkart"
                }
            )
        return image_product_page



