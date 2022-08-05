from bs4 import BeautifulSoup
import requests
import pandas as pd

###################### www.bloomeria.ro ######################

def get_contents_as_dictionary(full_string_contents):
    contents_dictionary = {}
    split_contents = full_string_contents.strip().split(',')

    for i in range(0, len(split_contents)):
        split_content_element = split_contents[i].strip().split(' ')
        for j in range(0, len(split_content_element)):
            if split_content_element[j].isdigit():
                if split_content_element[j + 1] == '':
                    content_name = split_content_element[j + 2].capitalize()
                elif split_content_element[j + 1].lower() == 'de':
                    content_name = split_content_element[j + 3].capitalize()
                else:
                    content_name = split_content_element[j + 1].capitalize()
                contents_dictionary.update({content_name.capitalize(): int(split_content_element[j])})
    print(contents_dictionary)
    return contents_dictionary


website_pages_url = 'https://bloomeria.ro/buchete-de-flori?p='
products_names = []
products_prices = []
products_contents = []
page_number = 1

while True:
    current_page_url = website_pages_url + str(page_number)
    page_html_document = requests.get(current_page_url).text
    soup = BeautifulSoup(page_html_document, 'lxml')
    if soup.find('li', attrs={"class": "item pages-item-next"}) is None:
        break

    products_images = soup.find_all('div', attrs={"class": "product photo product-item-photo"})
    for image in products_images:
        try:
            product_url = image.find('a')['href']
            product_html_document = requests.get(product_url).text
            product_soup = BeautifulSoup(product_html_document, 'lxml')
            if product_soup.find('td', attrs={'data-th': 'Compozitie'}) is None:
                continue
            contents = get_contents_as_dictionary(product_soup.find('td', attrs={'data-th': 'Compozitie'}).text)
            if len(contents) == 0:
                continue
            products_names.append(product_soup.find('span', attrs={'itemprop': 'name'}).text)
            products_prices.append(float(product_soup.find('span', attrs={'class': 'price'}).text[0:-7]))
            products_contents.append(contents)

        except:
            print("Corrupt data, skipping...")

    page_number += 1

pd.DataFrame({
    'Product name': products_names,
    'Price (RON)': products_prices,
    'Contents': products_contents
}).to_csv('../outputs/FlowerShop_2.csv', index=False)
