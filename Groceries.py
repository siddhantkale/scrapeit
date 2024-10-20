import requests
from bs4 import BeautifulSoup

class Blinkit:
    url = "https://blinkit.com/s/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    params = {}

    def __init__(self, user_search):
        self.params = {'q': user_search}

    def get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        while response.status_code == 503:
            response = requests.get(self.url, headers=self.headers, params=self.params)
        return response


    def map_images(self):
        response = self.get_response()
        soup = BeautifulSoup(response.text, 'html.parser')
        product_divs = soup.find_all("div",class_="ProductsContainer__SearchProductsListContainer-sc-1k8vkvc-1")
        divs = []
        for div in product_divs:
            all_as = div.find_all("a")
            for a in all_as:
                divs.append(a)
        blinkit_map = []
        for div in divs:
            product_price = div.find("div",class_="Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10")
            product_price = product_price.find("div").text
            product_price = "₹" + product_price.split("₹")[1]
            product_name = div.find("div","Product__UpdatedTitle-sc-11dk8zk-9").text
            product_url = "https://blinkit.com/" + div["href"]
            blinkit_map.append({"product_link": product_url, "product_name": product_name
                                        ,"product_price": product_price})
        return blinkit_map







