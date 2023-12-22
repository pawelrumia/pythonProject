import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import StandardScaler

# fetch dataset
magic_gamma_telescope = fetch_ucirepo(id=159)

# data (as pandas dataframes)
X = magic_gamma_telescope.data.features
y = magic_gamma_telescope.data.targets

# metadata
print(magic_gamma_telescope.metadata)

# variable information
print(magic_gamma_telescope.variables)

columns = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv('collections/magic04.data', names=columns)

df["class"] = (df["class"] == "g").astype(int)
print(df.head())

for value in columns[:-1]:
    plt.hist(df[df["class"] == 1][value], color='blue', label='gamma', alpha=0.7, density=True)
    plt.hist(df[df["class"] == 0][value], color='red', label='hadron', alpha=0.7, density=True)
    plt.title(value)
    plt.ylabel("Probability")
    plt.xlabel(value)
    plt.legend()
    # plt.show()

#train, validation and test datasets

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    data = np.hstack((X, np.reshape(y, (-1, 1))))
    return data, X, y

print(train)
len(train[train["class"] == 1])