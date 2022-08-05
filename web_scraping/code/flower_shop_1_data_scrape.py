from bs4 import BeautifulSoup
import requests
import pandas as pd

###################### www.florarie.ro ######################

main_website_url = "https://www.florarie.ro"
website_pages_url = 'https://www.florarie.ro/buchete-flori/pagina/'
page_number = 1
products_names = []
products_prices = []
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

        products_names.append(soup.find('div', attrs={"class": "info"}).find('h1').text)
        sizes_tags = soup.find_all('div', attrs={"class": "marime"})
        for tag in sizes_tags:
            if tag.find('input')['value'] == 'normal':
                products_prices.append(float(tag.find('span').text.split()[0]))
                full_content = tag.find('div', attrs={"class": "continut"}).text.strip().split(',')

                products_contents_dictionary = {}
                for content in full_content:
                    quantity, content_name = int(content.strip().split(' ', 1)[0]), content.strip().split(' ', 1)[1]
                    products_contents_dictionary.update({content_name.capitalize(): quantity})
                products_contents.append(products_contents_dictionary)

        print("Product " + str(current_product_number) + "...")
        current_product_number += 1

    page_number += 1

pd.DataFrame({
    'Product name': products_names,
    'Price (RON)': products_prices,
    'Contents': products_contents
}).to_csv('../outputs/FlowerShop_1.csv', index=False)
