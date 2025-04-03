from app import app
from dash.testing.composite import DashComposite
import os

def test_header_present(dash_duo: DashComposite):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("header-1", timeout=10)
    assert dash_duo.find_element("#header-1")

def test_visualisation_present(dash_duo: DashComposite):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("fig-1-line-chart", timeout=10)
    assert dash_duo.find_element("#fig-1-line-chart")


def test_region_picker_present(dash_duo: DashComposite):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("fig-1-region-picker", timeout=10)
    assert dash_duo.find_element("#fig-1-region-picker")