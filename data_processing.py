import pandas as pd
import os

data_folder = "data"
file_names = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

# List to hold DataFrames
dfs = []

for file_name in file_names:
    file_path = os.path.join(data_folder, file_name)
    df = pd.read_csv(file_path)

    df = df[df["product"] == "pink morsel"]

    # 🔧 Convert price string to float
    df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)


    # ✅ Calculate sales correctly
    df["sales"] = df["quantity"] * df["price"]

    df_cleaned = df[["sales", "date", "region"]]

    dfs.append(df_cleaned)

final_df = pd.concat(dfs, ignore_index=True)

output_path = os.path.join("data", "cleaned_sales_data.csv")
final_df.to_csv(output_path, index=False)
print(f"Cleaned data saved to: {output_path}")
