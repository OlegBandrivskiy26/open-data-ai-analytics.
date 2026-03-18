import os
import pandas as pd

DATA_PATH = "data/raw/data.csv"


def check_data_quality(path):
    if not os.path.exists(path):
        print("File not found:", path)
        return

    df = pd.read_csv(path)

    print("=== DATA INFO ===")
    print(df.info())

    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum())

    print("\n=== DUPLICATES ===")
    print(df.duplicated().sum())

    print("\n=== DESCRIBE ===")
    print(df.describe())

    print("\n=== COLUMN TYPES ===")
    print(df.dtypes)


if __name__ == "__main__":
    check_data_quality(DATA_PATH)