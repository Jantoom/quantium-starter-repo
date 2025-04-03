from globals import csv_paths, out_path
import pandas


def format_data(export=True):
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

    if export:
        out_data.to_csv(out_path, index=False)

    return out_data
