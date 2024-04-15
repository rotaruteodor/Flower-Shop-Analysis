import pandas as pd
from utils.dataframe_manager import get_flowershops_dataframes, PRODUCT_CURRENT_PRICE_HEADER, DIFFERENCE_HEADER, \
    DIFFERENCE_PERCENTAGE_HEADER

total_price_of_other_N_bouquet_contents = 11


def get_N_price(row):
    total = total_price_of_other_N_bouquet_contents
    for flower_type in row.Contents:
        if flowershop_N_flower_prices.get(flower_type) is None:
            return -1
        total += flowershop_N_flower_prices.get(flower_type) * row.Contents.get(flower_type)
    return float(total)


def export_comparison(flowershop_df, title_of_exported_csv):
    COMPETITOR_CURRENT_PRICE_HEADER = 'Competitor ' + PRODUCT_CURRENT_PRICE_HEADER
    PRICE_N_HEADER = 'Price N (RON)'

    flowershop_df.rename(columns={PRODUCT_CURRENT_PRICE_HEADER: COMPETITOR_CURRENT_PRICE_HEADER}, inplace=True)
    flowershop_df[PRICE_N_HEADER] = flowershop_df.apply(get_N_price, axis=1)
    flowershop_df[DIFFERENCE_HEADER] = round(flowershop_df[PRICE_N_HEADER] - flowershop_df[COMPETITOR_CURRENT_PRICE_HEADER])
    flowershop_df[DIFFERENCE_PERCENTAGE_HEADER] = flowershop_df[DIFFERENCE_HEADER] / flowershop_df[COMPETITOR_CURRENT_PRICE_HEADER]
    flowershop_df.drop(flowershop_df[flowershop_df[PRICE_N_HEADER] == -1].index).to_csv(title_of_exported_csv)


df_flowershop_N_flower_prices = pd.read_csv("Flowershop_N_flower_prices.csv")
flowershop_N_flower_prices = dict(zip(df_flowershop_N_flower_prices.flower, df_flowershop_N_flower_prices.price))

flowershop_1_df, flowershop_2_df, flowershop_3_df = get_flowershops_dataframes()
export_comparison(flowershop_1_df, "outputs/FlowerShop_1_Comparison.csv")
export_comparison(flowershop_2_df, "outputs/FlowerShop_2_Comparison.csv")
export_comparison(flowershop_3_df, "outputs/FlowerShop_3_Comparison.csv")
