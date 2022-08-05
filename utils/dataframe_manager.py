import pandas as pd
from ast import literal_eval


def get_flowershops_dataframes():
    flowershop_1_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\web_scraping\\outputs\\FlowerShop_1.csv', index_col=0)
    flowershop_1_df['Contents'] = flowershop_1_df['Contents'].map(literal_eval)
    flowershop_2_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\web_scraping\\outputs\\FlowerShop_2.csv', index_col=0)
    flowershop_2_df['Contents'] = flowershop_2_df['Contents'].map(literal_eval)
    flowershop_3_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\web_scraping\\outputs\\FlowerShop_3.csv', index_col=0)
    flowershop_3_df['Contents'] = flowershop_3_df['Contents'].map(literal_eval)
    return flowershop_1_df, flowershop_2_df, flowershop_3_df


def get_flowershops_comparisons_dataframes():
    flowershop_1_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\price_comparison\\outputs\\FlowerShop_1_Comparison.csv', index_col=0)
    flowershop_2_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\price_comparison\\outputs\\FlowerShop_2_Comparison.csv', index_col=0)
    flowershop_3_df = pd.read_csv('C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\price_comparison\\outputs\\FlowerShop_3_Comparison.csv', index_col=0)
    return flowershop_1_df, flowershop_2_df, flowershop_3_df
