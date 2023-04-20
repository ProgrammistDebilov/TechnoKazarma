from dash import *
from dash_leaflet import TileLayer, Map, LocateControl
from dash.dependencies import Output, Input
import Backend.work_db as db
from geopy.geocoders import Photon
# Create a Dash app
app = dash.Dash(__name__)
# define icons
icon_green = {
    "iconUrl": 'https://i.ibb.co/SmZPXPc/25962fdc-4e92-4303-97c6-ea2c7e52d4cc.png',
    "iconSize": [38, 95],  # size of the icon
}
icon_red = {
    "iconUrl": 'https://i.ibb.co/dKP3Lm5/2c4a6b06-72cd-49e1-950d-ec2d5295d9b5.png',
    "iconSize": [38, 95],  # size of the icon
}
icon_yellow = {
    "iconUrl": 'https://i.ibb.co/zfvg2jM/f18848bd-2052-47cd-9679-8651bd705346.png',
    "iconSize": [38, 95],  # size of the icon
}
#define geolocator
geolocator = Photon(user_agent="MyApp")

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
        max_num = i
    for i,j in enumerate(db.return_orders()):
        location = geolocator.geocode(j['adress'])
        k = max_num + i + 1
        markers.append({'props': {'children': {'props': {'children': location.address}, 'type': 'Tooltip', 'namespace': 'dash_leaflet'}, 'id': str(k), 'position':[ location.latitude, location.longitude] }, 'type': 'Marker', 'namespace': 'dash_leaflet'})
    return [markers,name_login]


if __name__ == '__main__':
    app.run_server()

