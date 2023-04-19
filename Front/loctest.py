import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_leaflet as dl
import random

# Define initial location for marker
marker_location = [51.5074, -0.1278]

# Define function to generate random marker location
def generate_marker_location():
    lat = random.uniform(-90, 90)
    lng = random.uniform(-180, 180)
    print(lat,lng)
    return [lat, lng]

# Define Dash app
app = dash.Dash(__name__)

# Define map component
map_component = dl.Map(
    center=marker_location,
    zoom=10,
    children=[
        dl.Marker(
            position=marker_location,
            id="marker",
            children=[
                dl.Tooltip("My Marker")
            ]
        )
    ]
)

# Define callback function to update marker location
@app.callback(
    dash.dependencies.Output("marker", "position"),
    [dash.dependencies.Input("interval", "n_intervals")]
)
def update_marker_position(n):
    return generate_marker_location()

# Define layout
# app.layout = html.Div([
#     map_component,
#     html.Br(),
#     dcc.Interval(id="interval", interval=2000),
# ])

# Run app
if __name__ == '__main__':
    app.run_server()