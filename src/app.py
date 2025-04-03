# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from globals import formatted_csv_path
from data import format_data
import plotly.express as px
import pandas as pd
import os

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
if os.path.exists(formatted_csv_path):
    formatted_data = pd.read_csv(formatted_csv_path)
else:
    formatted_data = format_data()


fig_1_data = (
    formatted_data.groupby("Date", as_index=False)["Sales"]
    .sum()
    .sort_values(by=["Date"])
)

fig_1 = px.line(fig_1_data, x="Date", y="Sales")

app.layout = html.Div(
    children=[
        html.H1(children="Soul Food Pink Morsel Sales"),
        html.Div(
            children="""
        Visualisation of daily sales data for Soul Food's Pink Morsel product.
    """
        ),
        dcc.Graph(id="example-graph", figure=fig_1),
    ]
)
