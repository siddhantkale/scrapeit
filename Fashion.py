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




    def map_images(self):
        response = self.get_response()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_search_result = soup.find_all("div", class_="_75nlfW")
        product_divs = [
            a.find_all("div", class_="_1sdMkc LFEi7Z") for a in all_search_result
        ]
        flipkart_map = []
        for div in product_divs:
            for a in div:
                product_page_link = "https://www.flipkart.com" + a.find("a")["href"]

                product_image = a.find("img")["src"]
                product_price = a.find("div", class_="Nx9bqj").text
                product_name = a.find("a",class_="WKTcLC").text
                flipkart_map.append({"product_link": product_page_link, "image_link": product_image
                                        , "product_price": product_price,'product_name':product_name, "site":"Flipkart"})
        return flipkart_map


class Amazon:
    url = "https://amazon.in/s"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
        "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }
    params = {}
    def __init__(self,user_search):
        self.params = {'k': user_search}

    def get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        while response.status_code == 503:
            response = requests.get(self.url, headers=self.headers, params=self.params)
        return response




    def map_images(self):
        response = self.get_response()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_search_result = soup.find_all("div",class_="sg-col-inner")
        amazon_map = []
        for div in all_search_result:
            if div.find("span",class_ = "a-price-whole")==None:
                continue
            product_price =  "₹" + div.find("span",class_ ="a-price-whole").text
            product_page_link = "https://www.amazon.in" + div.find("a",class_="a-link-normal s-no-outline")["href"]
            product_image = div.find("img",class_ = "s-image")["src"]
            product_name = div.find("span",class_="a-size-base-plus a-color-base a-text-normal").text
            amazon_map.append({"product_link": product_page_link, "image_link": product_image
                                        , "product_price": product_price,'product_name':product_name, "site": "Amazon"})

        return amazon_map







