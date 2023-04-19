import dash
import dash_leaflet as dl
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_core_components as dcc
import random
import time

# create the Dash app
app = dash.Dash(__name__)

# define the initial marker location
marker_location = [38.9072, -77.0369]

# create the map
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),
        dl.Marker(position=marker_location, id='marker'),
            dcc.Interval(
            id='interval-component',
            interval=2000,
            n_intervals=0
    )
    ], style={'width': '100%', 'height': '50vh'}, center=marker_location, zoom=10),
])

# define the marker update function
def update_marker_location():
    # generate a random location within the DC area
    new_location = [38.9 + random.uniform(-0.1, 0.1), -77.0 + random.uniform(-0.1, 0.1)]
    return new_location

# update the marker location every 5 seconds
@app.callback(Output('marker', 'position'), Input('marker', 'id'))
def update_location(id):
    while True:
        time.sleep(5)
        new_location = update_marker_location()
        return new_location

if __name__ == '__main__':
    app.run_server(debug=True)
