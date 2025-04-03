from globals import RAW_CSV_PATHS, FORMATTED_CSV_PATH
import pandas as pd


def format_data(export=True):
    formatted_data = pd.DataFrame()

    for csv_path in RAW_CSV_PATHS:
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
        formatted_data.to_csv(FORMATTED_CSV_PATH, index=False)

    return formatted_data
