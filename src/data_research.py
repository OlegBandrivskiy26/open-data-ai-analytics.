import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_PATH = "data/raw/data.csv"


def load_data(path):
    if not os.path.exists(path):
        print("File not found")
        return None

    df = pd.read_csv(path)
    return df


def basic_analysis(df):
    print("Shape:", df.shape)
    print(df.head())
    print(df.describe())


def simple_plot(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) >= 2:
        x = numeric_cols[0]
        y = numeric_cols[1]

        plt.scatter(df[x], df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title("Scatter plot")
        plt.show()


def simple_model(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        print("Not enough numeric columns")
        return

    X = df[[numeric_cols[0]]]
    y = df[numeric_cols[1]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    print("Model score:", score)


if __name__ == "__main__":
    df = load_data(DATA_PATH)

    if df is not None:
        basic_analysis(df)
        simple_plot(df)
        simple_model(df)