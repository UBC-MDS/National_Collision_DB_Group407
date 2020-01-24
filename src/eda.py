""" Script used to import CSV data from a publicly accessible URL or relative file path.

Usage:
  eda.py --read_path=<read_path> --write_path=<write_path>

Example:
  python eda.py --read_path=../data/cleaned_train_data.csv --write_path=../results/

"""
from pandas.plotting import table
from docopt import docopt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(read_path, write_path):
    df = pd.read_csv(read_path)
    df = df.drop(["Unnamed: 0","C_SEV_2"], axis=1)
    fatal = df[df.C_SEV_1 == 1]
    non_fatal = df[df.C_SEV_1 == 0]
    df_names = list(df.columns)

    # Number of Fatal Crashes Per Hour of Day
    hour_columns = [s for s in df_names if "C_HOUR" in s]
    hours = fatal[hour_columns].sum().sort_values(ascending=False).index
    hour_index_names = [i[-2:].replace("_", "") for i in hours]
    plt.bar(hour_index_names,
            fatal[hour_columns].sum().sort_values(ascending=False))
    plt.title("Hour of Day and Fatal Crashes")
    plt.xlabel("Hour of Day")
    plt.ylabel("Fatal Crashes")
    plt.savefig(write_path + "fatal_hourly_crashes.png")

    # Number of Non-Fatal Crashes Per Hour of Day
    hour_columns = [s for s in df_names if "C_HOUR" in s]
    hours = non_fatal[hour_columns].sum().sort_values(ascending=False).index
    hour_index_names = [i[-2:].replace("_", "") for i in hours]
    plt.bar(hour_index_names,
            non_fatal[hour_columns].sum().sort_values(ascending=False))
    plt.title("Hour of Day and Non-Fatal Crashes")
    plt.xlabel("Hour of Day")
    plt.ylabel("Non-Fatal Crashes")
    plt.savefig(write_path + "non_fatal_hourly_crashes.png")

    # Top 10 Fatal Features
    fatal_features = pd.DataFrame(fatal.sum().sort_values(ascending=False).head(10))[1:]
    fatal_features.rename(columns={0: "fatal_crashes"}, inplace=True)
    fatal_features.plot.bar()
    plt.title("Top 10 Features Most Linked to Fatality")
    plt.ylabel("Fatalities")
    plt.xticks(rotation='45')
    plt.tight_layout()
    plt.savefig(write_path + "fatal_features.png")

    # Top 10 Features Non-Fatal
    non_fatal_features = pd.DataFrame(non_fatal.sum().sort_values(ascending=False).head(10))[1:]
    non_fatal_features.rename(columns={0: "non_fatality_crashes"}, inplace=True)
    non_fatal_features.plot.bar()
    plt.title("Top 10 Features Most Linked to Non-Fatal Crashes")
    plt.ylabel("Non-Fatal Crashes")
    plt.xticks(rotation='45')
    plt.tight_layout()
    plt.savefig(write_path + "non_fatal_features.png")



if __name__ == "__main__":
    main(opt["--read_path"], opt["--write_path"])
