import pandas as pd
from utils.dataframe_manager import get_flowershops_dataframes


total_price_of_other_N_bouquet_contents = 11


def get_N_price(row):
    total = total_price_of_other_N_bouquet_contents
    for flower_type in row.Contents:
        if flowershop_N_flower_prices.get(flower_type) is None:
            return -1
        total += flowershop_N_flower_prices.get(flower_type) * row.Contents.get(flower_type)
    return float(total)


def export_comparison(flowershop_df, title_of_exported_csv):
    flowershop_df.rename(columns={'Price (RON)': 'Competitor Price (RON)'}, inplace=True)
    flowershop_df["Price N (RON)"] = flowershop_df.apply(get_N_price, axis=1)
    flowershop_df["Difference"] = round(flowershop_df['Price N (RON)'] - flowershop_df['Competitor Price (RON)'])
    flowershop_df["Difference (%)"] = flowershop_df['Difference'] / flowershop_df['Competitor Price (RON)']
    flowershop_df.drop(flowershop_df[flowershop_df['Price N (RON)'] == -1].index).to_csv(title_of_exported_csv)


df_flowershop_N_flower_prices = pd.read_csv("C:\\Users\\ADMIN\\PycharmProjects\\FlowerShopsAnalysis\\price_comparison\\flowershop_N_data\\Flowershop_N_flower_prices.csv")
flowershop_N_flower_prices = dict(zip(df_flowershop_N_flower_prices.flower, df_flowershop_N_flower_prices.price))

flowershop_1_df, flowershop_2_df, flowershop_3_df = get_flowershops_dataframes()
export_comparison(flowershop_1_df, "FlowerShop_1_Comparison.csv")
export_comparison(flowershop_2_df, "FlowerShop_2_Comparison.csv")
export_comparison(flowershop_3_df, "FlowerShop_3_Comparison.csv")
