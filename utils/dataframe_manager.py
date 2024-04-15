import pandas as pd
from ast import literal_eval


PRODUCT_ID_HEADER = 'Product ID'
PRODUCT_NAME_HEADER = 'Product name'
PRODUCT_CURRENT_PRICE_HEADER = 'Price (RON)'
PRODUCT_ORIGINAL_PRICE_HEADER = 'Original ' + PRODUCT_CURRENT_PRICE_HEADER
PRODUCT_CONTENTS_HEADER = 'Contents'
DIFFERENCE_HEADER = 'Difference'
DIFFERENCE_PERCENTAGE_HEADER = 'Difference (%)'

def get_flowershops_dataframes():
    flowershop_1_df = pd.read_csv('../web_scraping/outputs/FlowerShop_1.csv', index_col=0)
    flowershop_1_df[PRODUCT_CONTENTS_HEADER] = flowershop_1_df[PRODUCT_CONTENTS_HEADER].map(literal_eval)
    flowershop_2_df = pd.read_csv('../web_scraping/outputs/FlowerShop_2.csv', index_col=0)
    flowershop_2_df[PRODUCT_CONTENTS_HEADER] = flowershop_2_df[PRODUCT_CONTENTS_HEADER].map(literal_eval)
    flowershop_3_df = pd.read_csv('../web_scraping/outputs/FlowerShop_3.csv', index_col=0)
    flowershop_3_df[PRODUCT_CONTENTS_HEADER] = flowershop_3_df[PRODUCT_CONTENTS_HEADER].map(literal_eval)
    return flowershop_1_df, flowershop_2_df, flowershop_3_df


def get_flowershops_comparisons_dataframes():
    flowershop_1_df = pd.read_csv('../price_comparison/outputs/FlowerShop_1_Comparison.csv', index_col=0)
    flowershop_2_df = pd.read_csv('../price_comparison/outputs/FlowerShop_2_Comparison.csv', index_col=0)
    flowershop_3_df = pd.read_csv('../price_comparison/outputs/FlowerShop_3_Comparison.csv', index_col=0)
    return flowershop_1_df, flowershop_2_df, flowershop_3_df
