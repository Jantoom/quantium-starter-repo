import pandas

csv_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]
out_path = "data/out.csv"
out_data = pandas.DataFrame()

for csv_path in csv_paths:
    temp = pandas.read_csv(csv_path)
    out_data = pandas.concat(
        [
            out_data,
            temp.loc[temp["product"] == "pink morsel"]
            .replace({"price": r"[^\d.]"}, "", regex=True)
            .assign(Sales=lambda x: x.quantity * x.price.astype(float))
            .drop(columns=temp.columns.drop(labels=["date", "region"]))
            .rename(columns={"date": "Date", "region": "Region"})
            .reindex(columns=["Sales", "Date", "Region"]),
        ]
    )

out_data.to_csv(out_path, index=False)
