import pandas as pd
import os

def load_data(file_name):
    \"\"\"
    Loads a dataset from the data directory.
    \"\"\"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", file_name)
    return pd.read_csv(data_path)

if __name__ == "__main__":
    df = load_data("customer_churn.csv")
    print(f"Loaded dataset with shape: {df.shape}")
