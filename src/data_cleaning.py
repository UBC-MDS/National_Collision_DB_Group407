import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# read the data from csv file 
df = pd.read_csv("../data/raw_data.csv")

# drop irrelavant columns, split data into train and test sets
X = df.drop(["C_YEAR", "C_VEHS", "C_CONF", "V_ID", "V_YEAR",
             "P_ID", "P_PSN", "P_ISEV", "P_USER", "C_CASE", "C_SEV", "P_SEX", "P_AGE", "P_SAFE"], axis=1)
y = df["C_SEV"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=407)

# clean the train data, dropping rows with unknown/string values and convert data frame to numeric type
combined_train = pd.concat([X_train, y_train], axis=1)
cleaned = combined_train.apply(pd.to_numeric, errors='coerce').dropna(axis=0).astype(int)

# clean the test data, dropping rows with unknown/string values and convert data frame to numeric type
combined_test = pd.concat([X_test, y_test], axis=1)
cleaned_test = combined_test.apply(pd.to_numeric, errors='coerce').dropna(axis=0).astype(int)

# get dummy variables for the cleaned data
final_cleaned = pd.get_dummies(cleaned.astype(str))
final_cleaned_test = pd.get_dummies(cleaned_test.astype(str))

# save final data frame as csv file
final_cleaned.to_csv("../data/cleaned_train_data.csv")
final_cleaned_test.to_csv("../data/cleaned_test_data.csv")