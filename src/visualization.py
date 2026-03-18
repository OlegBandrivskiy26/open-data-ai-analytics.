import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/raw/data.csv"
FIG_PATH = "reports/figures/plot.png"


def visualize(path):
    if not os.path.exists(path):
        print("File not found")
        return

    df = pd.read_csv(path)

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        print("Not enough numeric columns")
        return

    x = numeric_cols[0]
    y = numeric_cols[1]

    plt.figure()
    plt.plot(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Data visualization")

    os.makedirs("reports/figures", exist_ok=True)
    plt.savefig(FIG_PATH)

    print("Saved to", FIG_PATH)


if __name__ == "__main__":
    visualize(DATA_PATH)