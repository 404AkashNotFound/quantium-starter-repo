import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_sales_data.csv')

# Initialize the app
app = dash.Dash(__name__)

# Layout with title and line chart
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer"),
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df,
            x='date',
            y='sales',
            title='Pink Morsel Sales Over Time',
            labels={'sales': 'Sales ($)', 'date': 'Date'},
            markers=True
        )
    )
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)  # Changed here
