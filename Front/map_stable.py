from dash import *
from dash_leaflet import Marker, TileLayer, Map, Tooltip, LocateControl
from dash.dependencies import Output, Input
import Backend.work_db as db
from geopy.geocoders import Nominatim
# Create a Dash app
app = dash.Dash(__name__)
# define icons
icon1 = {
    "iconUrl": 'https://i.ibb.co/YcnsYpn/shreks.png',
    "iconSize": [38, 95],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
icon2 = {
    "iconUrl": 'https://i.ibb.co/ZKJYbB1/patrik.png',
    "iconSize": [38, 95],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
icon3 = {
    "iconUrl": 'https://i.ibb.co/bJb8bZC/gosling.png',
    "iconSize": [38, 95],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
#define geolocator
geolocator = Nominatim(user_agent="MyApp")

# Define the layout of the app
app = Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)
app.layout = html.Div([
    Map( style={'width': 'auto', 'height': '95vh', 'margin': "auto", "display": "block"}, zoom=3, id= 'map'),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    ),
    html.Div(id="text"),
    dcc.Location(id='url')
])

    
# Define a callback to update maps children

@app.callback(    
    [
        Output("map", "children"),
        Output("text", "children")
    ],
    [
        Input("interval","n_intervals"),
        Input("url", "pathname"),
        Input("map","location_lat_lon_acc"),
    ],
)
# function to update every single thing
def update_every_fucking_thing(n,k,j):
    login = k[1::]
    name_login = "Ваш логин: " + login
    if j != None:
        db.insert_location(login, j[0], j[1])
    markers = [TileLayer(), LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})]
    for i,j in enumerate(db.return_installers()):
        markers.append({'props': {'children': {'props': {'children': j['login']}, 'type': 'Tooltip', 'namespace': 'dash_leaflet'}, 'id': str(i), 'position': db.return_location(j['login'])}, 'type': 'Marker', 'namespace': 'dash_leaflet'})
    return [markers,name_login]


if __name__ == '__main__':
    app.run_server()

