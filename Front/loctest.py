import dash
import dash_html_components as html
import dash_leaflet as dl
import dash_core_components as dcc
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import random

# Create a Dash app
app = dash.Dash(__name__)

# Define the initial marker position
marker_position = [random.randint(-90,90), random.randint(-180,180)]

# Define a list of marker positions to loop through
marker_positions = [
    [37.7749, -122.4194],
    [40.7128, -74.0060],
    [51.5074, -0.1278],
    [35.6895, 139.6917],
]

# Define the layout of the app
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),
        dl.Marker(id='marker', position=marker_position),
    ], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, zoom=10),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    )
])

# Define a callback to update the marker position
@app.callback(Output('marker', 'position'), [Input('interval', 'n_intervals')])
def update_marker_position(n):
    # Get the next marker position from the list
    return [random.randint(-90,90), random.randint(-180,180)]

# Run the app
if __name__ == '__main__':
    app.run_server()
