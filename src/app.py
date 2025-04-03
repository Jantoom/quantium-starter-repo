# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from globals import FORMATTED_CSV_PATH
from data import format_data
import plotly.express as px
import pandas as pd
import os

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
if os.path.exists(FORMATTED_CSV_PATH):
    formatted_data = pd.read_csv(FORMATTED_CSV_PATH)
else:
    formatted_data = format_data()


fig_1_data = (
    formatted_data.groupby("Date", as_index=False)["Sales"]
    .sum()
    .sort_values(by=["Date"])
)

fig_1 = px.line(fig_1_data, x="Date", y="Sales")

app.layout = html.Div(
    [
        html.H1("Soul Food Pink Morsel Sales"),
        html.Span("Sales visualisation for Soul Food's Pink Morsel product."),
        dcc.Graph(id="pink-morsel-sales-line-chart", figure=fig_1),
    ]
)
