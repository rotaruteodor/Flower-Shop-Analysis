from utils.dataframe_manager import get_flowershops_dataframes
import matplotlib.pyplot as plt

labels = ["Average", "St dev", "Lowest", "25% are under", "50% are under", "75% are under", "Highest"]


def configure_prices_stats_barchart(prices, title, index=1):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    values = list(map(int, prices.describe().apply("{0:.0f}".format).values))[1:]
    plt.figure(index)
    plt.barh(labels, values)
    plt.title(title)
    plt.ylabel('Stat')
    plt.xlabel('Price (RON)')
    for i, v in enumerate(values):
        ax.text(v + 3, i, str(v), color='green', fontweight='bold')


flowershop_1_df, flowershop_2_df, flowershop_3_df = get_flowershops_dataframes()
configure_prices_stats_barchart(flowershop_1_df['Price (RON)'], "Flower Shop 1 - Prices stats", 1)
configure_prices_stats_barchart(flowershop_2_df['Price (RON)'], "Flower Shop 2 - Prices stats", 2)
configure_prices_stats_barchart(flowershop_3_df['Price (RON)'], "Flower Shop 3 - Prices stats", 3)
plt.show()
