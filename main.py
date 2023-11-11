
import requests
from bs4 import BeautifulSoup
import lxml

url_base = "https://rozetka.com.ua/ua/tablets/c130309/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
session = requests.Session()

for j in range(1, 68):
    print(f"Page {j}\n\n")
    page_url = f"{url_base}page={j}/"
    response = session.get(page_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for i in all_products:
            title = i.find('span', class_='goods-tile__title')
            try:
                if i.find('div', class_='goods-tile__price--old price--gray ng-star-inserted'):
                    original_price = i.find('div', class_="goods-tile__price--old price--gray ng-star-inserted")
                    price = i.find('span', class_='goods-tile__price-value')
                    print(f"Знижкова цiна: {price.text}, на товар {title.text}, оригiнальна цiна: {original_price.text}\n")
            except ValueError:
                print("Знижки нема")