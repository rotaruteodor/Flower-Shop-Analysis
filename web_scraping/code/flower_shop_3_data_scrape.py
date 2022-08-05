from bs4 import BeautifulSoup
import requests
import pandas as pd

###################### www.florarieonline.com ######################

main_website_url = "https://www.florarieonline.com/buchete-cu-flori/toate"

products_names = []
products_prices = []
products_contents = []

html_document = requests.get(main_website_url).text
soup = BeautifulSoup(html_document, 'lxml')

products_list = soup.find('ul', attrs={"class": "produse"})
products_list_items_link_tags = products_list.find_all('a')
products_list_items_price_tags = products_list.find_all('div', attrs={"class": ["pret", "pret_redus"]})

for i in range(0, len(products_list_items_link_tags), 2):
    products_names.append(products_list_items_link_tags[i]['title'])
    try:
        products_prices.append(float(products_list_items_price_tags[int(i / 2)].find('p').text))
    except:
        products_prices.append(
            float(products_list_items_price_tags[int(i / 2)].find('p', attrs={"class": "pret"}).text))

    product_html_document = requests.get(products_list_items_link_tags[i]['href']).text
    soup = BeautifulSoup(product_html_document, 'lxml')

    tag = soup.find('label', attrs={"class": "s_radio", "for": "pret-1"})
    full_content = tag.find('div', attrs={"class": "price_content"}).text[10:].strip().split(' , ')

    products_contents_dictionary = {}
    for content in full_content:
        quantity_as_string = content[content.index("(") + 1: content.index(")")]
        content_name = content[:-len(quantity_as_string) - 2]
        products_contents_dictionary.update({content_name.capitalize(): quantity_as_string})
    products_contents.append(products_contents_dictionary)

pd.DataFrame({
    'Product name': products_names,
    'Price (RON)': products_prices,
    'Contents': products_contents
}).to_csv('../outputs/FlowerShop_3.csv', index=False)
