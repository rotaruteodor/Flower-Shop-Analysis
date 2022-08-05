from utils.dataframe_manager import get_flowershops_comparisons_dataframes
import pandas as pd
import matplotlib.pyplot as plt

labels = ["Average", "St dev", "Lowest", "25% are under", "50% are under", "75% are under", "Highest"]

def configure_price_differences_bar_chart(df_column, title):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    values = list(map(int, df_column.describe().apply("{0:.0f}".format).values))[1:]
    plt.barh(labels, values)
    plt.title(title)
    plt.ylabel('Stat')
    plt.xlabel('Diff')
    for i, v in enumerate(values):
        ax.text(v + 4, i, str(v), color='white', fontweight='bold')

df_f1, df_f2, df_f3 = get_flowershops_comparisons_dataframes()
df_all_flowershops = pd.concat([df_f1, df_f2, df_f3], ignore_index=False)

configure_price_differences_bar_chart(df_all_flowershops['Difference'], "Difference stats (RON)")
configure_price_differences_bar_chart(df_all_flowershops['Difference (%)'] * 100, "Difference stats (%)")
plt.show()


