from bs4 import BeautifulSoup
import requests
import pandas as pd

from utils.dataframe_manager import PRODUCT_CURRENT_PRICE_HEADER, PRODUCT_ORIGINAL_PRICE_HEADER, \
    PRODUCT_CONTENTS_HEADER, PRODUCT_NAME_HEADER, PRODUCT_ID_HEADER

###################### www.florarie.ro ######################

main_website_url = "https://www.florarie.ro"
website_pages_url = 'https://www.florarie.ro/buchete-flori/pagina/'
page_number = 1
products_ids = []
products_names = []
products_current_prices = []
products_original_prices = []
products_contents = []
current_product_number = 1

while True:
    current_page_url = website_pages_url + str(page_number)
    html_document = requests.get(current_page_url).text
    soup = BeautifulSoup(html_document, 'lxml')

    flowers_images = soup.find_all('div', attrs={"class": "floareImg"})
    if len(flowers_images) == 0:
        break

    products_urls = [flower_image.find('a')['href'] for flower_image in flowers_images]
    for url in products_urls:
        current_product_url = main_website_url + url
        product_html_document = requests.get(current_product_url).text
        soup = BeautifulSoup(product_html_document, 'lxml')

        products_ids.append(soup.find('div', attrs={"class": "info"}).find('h2').text.removeprefix("ID: #"))
        product_name = soup.find('div', attrs={"class": "info"}).find('b').text
        products_names.append(product_name)
        sizes_tags = soup.find_all('div', attrs={"class": "marime"})
        for tag in sizes_tags:
            if tag.find('input')['value'] == 'normal':
                currentPrice = float(tag.find('span', attrs={"class": "pret_normal"}).text.split()[0])
                products_current_prices.append(currentPrice)
                originalPriceHtmlTag = tag.find('span', attrs={"class": "redus redus_normal"})
                products_original_prices.append(float(originalPriceHtmlTag.text.split()[0])
                                                if originalPriceHtmlTag is not None
                                                else currentPrice)
                full_content = tag.find('div', attrs={"class": "continut"}).text.strip().split(',')
                products_contents_dictionary = {}
                for content in full_content:
                    quantity, content_name = int(content.strip().split(' ', 1)[0]), content.strip().split(' ', 1)[1]
                    products_contents_dictionary.update({content_name.capitalize(): quantity})
                products_contents.append(products_contents_dictionary)
        print("Saved product #" + str(current_product_number) + " - " + product_name)
        current_product_number += 1
    page_number += 1

pd.DataFrame({
    PRODUCT_ID_HEADER: products_ids,
    PRODUCT_NAME_HEADER: products_names,
    PRODUCT_CURRENT_PRICE_HEADER: products_current_prices,
    PRODUCT_ORIGINAL_PRICE_HEADER: products_original_prices,
    PRODUCT_CONTENTS_HEADER: products_contents
}).to_csv('../outputs/FlowerShop_1.csv', index=False)
