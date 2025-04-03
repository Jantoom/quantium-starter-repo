from globals import raw_csv_paths, formatted_csv_path
import pandas as pd


def format_data(export=True):
    formatted_data = pd.DataFrame()

    for csv_path in raw_csv_paths:
        temp = pd.read_csv(csv_path)
        formatted_data = pd.concat(
            [
                formatted_data,
                temp.loc[temp["product"] == "pink morsel"]
                .replace({"price": r"[^\d.]"}, "", regex=True)
                .assign(Sales=lambda x: x.quantity * x.price.astype(float))
                .drop(columns=temp.columns.drop(labels=["date", "region"]))
                .rename(columns={"date": "Date", "region": "Region"})
                .reindex(columns=["Sales", "Date", "Region"]),
            ]
        )

    if export:
        formatted_data.to_csv(formatted_csv_path, index=False)

    return formatted_data
