import dash_leaflet as dl
from dash import Dash, html, Output, Input

# The external stylesheet holds the location button icon.
app = Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)
app.layout = html.Div([
    dl.Map([dl.TileLayer(), dl.LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})],
           id="map", style={'width': '', 'height': '', 'margin': "auto", "display": "block"}),
    html.Div(id="text")
])


@app.callback(Output("text", "children"), [Input("map", "location_lat_lon_acc")])
def update_location(location):
    print("You are within {} meters of (lat,lon) = ({},{})".format(location[2], location[0], location[1]))


if __name__ == '__main__':
    app.run_server()