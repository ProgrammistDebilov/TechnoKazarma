from dash import Dash, html, Output, Input
import dash_html_components as html
import dash_leaflet as dl
import dash_core_components as dcc
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import random

# Create a Dash app
#app = dash.Dash(__name__)

# Define the initial marker position

# Define a list of marker positions to loop through
app = Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)

# Define the layout of the app
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),
        dl.Marker(id='marker', position=[random.randint(-90,90), random.randint(-180,180)]),
        dl.Marker(id = 'marker2', position=[random.randint(-90,90), random.randint(-180,180)]),
        dl.LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})
    ], style={'width': 'auto', 'height': '98vh', 'margin': "auto", "display": "block"}, zoom=10),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    ),
        html.Div(id="text")
])

# Define a callback to update the marker position
@app.callback(Output('marker', 'position'),Output('marker2', 'position'),Output("text", "children"), [Input('interval', 'n_intervals'),Input("map", "location_lat_lon_acc")])
def update_marker_position(n):
    print('cock')
    # Get the next marker position from the list
    return [[random.randint(-90,90), random.randint(-180,180)],[random.randint(-90,90), random.randint(-180,180)]]
def update_location(location):
    print("You are within {} meters of (lat,lon) = ({},{})".format(location[2], location[0], location[1]))

# Run the app
if __name__ == '__main__':
    app.run_server()
