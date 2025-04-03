# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output, callback
from globals import FORMATTED_CSV_PATH, COLORS
from data import format_data
import plotly.express as px
import pandas as pd
import os

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
if not os.path.exists(FORMATTED_CSV_PATH):
    format_data()

formatted_data = pd.read_csv(FORMATTED_CSV_PATH)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    id="header-1",
                    children="Soul Food Pink Morsel Sales",
                    style={"textAlign": "center", "color": COLORS["text"]},
                ),
                html.Div(
                    "Sales visualisation for Soul Food's Pink Morsel product.",
                    style={"textAlign": "center", "color": COLORS["text"]},
                ),
            ],
        ),
        html.Div(
            children=[
                html.H4("Region/s selected:", style={"paddingLeft": 30}),
                dcc.RadioItems(
                    id="fig-1-region-picker",
                    options=["All", "North", "South", "East", "West"],
                    value="All",
                    inline=True,
                    style={"paddingLeft": 30},
                ),
                dcc.Graph(id="fig-1-line-chart"),
            ],
            style={
                "display": "flex",
                "flexDirection": "column",
                "flexGrow": 1,
                "justifyContent": "center",
            },
        ),
    ],
    style={
        "backgroundColor": COLORS["background"],
        "display": "flex",
        "flexDirection": "column",
        "height": "100vh",
        "width": "100vw",
    },
)


@callback(Output("fig-1-line-chart", "figure"), Input("fig-1-region-buttons", "value"))
def update_figure_1(selected_region):
    accepted_regions = (
        [str.lower(selected_region)]
        if selected_region == None or selected_region != "All"
        else ["north", "south", "east", "west"]
    )
    figure_1_data = (
        formatted_data.loc[formatted_data["Region"].isin(accepted_regions)]
        .groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values(by=["Date"])
    )

    figure_1 = px.line(figure_1_data, x="Date", y="Sales")
    figure_1.update_layout(
        plot_bgcolor=COLORS["primary"],
        paper_bgcolor=COLORS["background"],
        font_color=COLORS["text"],
    )

    return figure_1
