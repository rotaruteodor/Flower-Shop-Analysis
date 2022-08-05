from utils.dataframe_manager import get_flowershops_dataframes
import pandas as pd

flowershop_1_df, flowershop_2_df, flowershop_3_df = get_flowershops_dataframes()

flowershop_1_all_flowers = set([flower for list in list(flowershop_1_df['Contents']) for flower in list])
flowershop_2_all_flowers = set([flower for list in list(flowershop_2_df['Contents']) for flower in list])
flowershop_3_all_flowers = set([flower for list in list(flowershop_3_df['Contents']) for flower in list])

all_flower_types_merged = list(flowershop_1_all_flowers.union(flowershop_2_all_flowers, flowershop_3_all_flowers))
all_flower_types_merged.sort()

pd.DataFrame({
    'Flower type': all_flower_types_merged,
}).to_csv('All flower types.csv', index=False)



