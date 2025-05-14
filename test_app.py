import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_duo_app(dash_duo):
    app = import_app("sales_app")  # Make sure this matches the renamed file
    dash_duo.start_server(app)
    return dash_duo

def test_header(dash_duo_app):
    header = dash_duo_app.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"

def test_visualization(dash_duo_app):
    graph = dash_duo_app.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker(dash_duo_app):
    region_picker = dash_duo_app.find_element("#region-filter")
    assert region_picker is not None
