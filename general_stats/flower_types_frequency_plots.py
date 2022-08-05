import matplotlib.pyplot as plt
from collections import Counter
from utils.dataframe_manager import get_flowershops_dataframes


def configure_frequency_barchart(contents, title, index=1):
    flowershop_1_all_flowers = [list(content.keys()) for content in contents]
    frequencies_dict = dict(Counter(i for sub in flowershop_1_all_flowers for i in set(sub)))
    frequencies_dict = dict(sorted(frequencies_dict.items(), key=lambda x: x[1], reverse=True))
    data = list(frequencies_dict.values())[0:12]
    labels = list(map(lambda kv: (kv[0] + '(' + str(kv[1]) + ')'), frequencies_dict.items()))[0:12]
    plt.figure(index)
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Flower')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.bar(range(len(data)), data)


flowershop_1_df, flowershop_2_df, flowershop_3_df = get_flowershops_dataframes()
configure_frequency_barchart(flowershop_1_df['Contents'], "Flower Shop 1 - Most popular flowers", 1)
configure_frequency_barchart(flowershop_2_df['Contents'], "Flower Shop 2 - Most popular flowers", 2)
configure_frequency_barchart(flowershop_3_df['Contents'], "Flower Shop 3 - Most popular flowers", 3)
plt.show()
