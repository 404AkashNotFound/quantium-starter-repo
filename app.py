import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_sales_data.csv')

# Ensure 'date' column is a datetime object for proper plotting
df['date'] = pd.to_datetime(df['date'])

# Initialize the app
app = dash.Dash(__name__)

# Layout with title, radio button for region filter, and line chart
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    
    # Radio button for filtering by region
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        labelStyle={'display': 'block'}
    ),
    
    # Line chart for sales data
    dcc.Graph(id='sales-line-chart')
])

# Callback to update the line chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_chart(region):
    # Filter data based on selected region
    if region != 'all':
        filtered_df = df[df['region'] == region]
    else:
        filtered_df = df
    
    # Create a line chart using Plotly
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Sales Data for {region.capitalize()} Region' if region != 'all' else 'Pink Morsel Sales Over Time',
        labels={'sales': 'Sales ($)', 'date': 'Date'},
        markers=True
    )
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales')
    
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
