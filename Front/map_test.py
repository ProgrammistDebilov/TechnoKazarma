from dash import *
from dash_leaflet import Marker, TileLayer, Map, Tooltip, LocateControl
from dash.dependencies import Output, Input
import Backend.work_db as db
from geopy.geocoders import Nominatim
# Create a Dash app
app = dash.Dash(__name__)
icon1 = {
    "iconUrl": 'https://i.ibb.co/YcnsYpn/shreks.png',
    "iconSize": [38, 38],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
icon2 = {
    "iconUrl": 'https://i.ibb.co/ZKJYbB1/patrik.png',
    "iconSize": [38, 38],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
icon3 = {
    "iconUrl": 'https://i.ibb.co/bJb8bZC/gosling.png',
    "iconSize": [38, 38],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
geolocator = Nominatim(user_agent="MyApp")

logins = []
locations = []
returns = []
login = "логин не передался"
callbacks = [Output('text', 'position')]
for i in db.return_installers():
        logins.append(i['login'])
for i in logins:
    locations.append(list(db.return_location(i)))

# Define a list of markers
markers = [TileLayer(), LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})]
for i, j in enumerate(locations):
    markers.append(Marker(id = str(i), position=list(j), children=Tooltip(logins[i])))
    max_num = i
#print(db.return_orders())

for i,j in enumerate(db.return_orders()):
    k = max_num+i+1
    location = geolocator.geocode(j['adress'])
    match j['state']:
        case -1:
            markers.append(Marker(id = str(k),icon= icon1, position=[location.latitude, location.longitude], children=Tooltip(location.address)))
        case 0:
            markers.append(Marker(id = str(k),icon= icon2, position=[location.latitude, location.longitude], children=Tooltip(location.address)))
        case 1:
            markers.append(Marker(id = str(k),icon= icon3, position=[location.latitude, location.longitude], children=Tooltip(location.address)))

# Define the layout of the app
app = Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)
app.layout = html.Div([
    Map(markers, style={'width': 'auto', 'height': '95vh', 'margin': "auto", "display": "block"}, zoom=3, id= 'map'),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    ),
    html.Div(id="text"),
    dcc.Location(id='url')
])

for i in range(len(markers)-2):
    callbacks.append(Output(str(i), "position"))

    
# Define a callback to update the markers position

@app.callback(    
        callbacks,
    [
        Input("interval","n_intervals"),
        Input("url", "pathname"),
        Input("map","location_lat_lon_acc")
    ],
)
def update_marker_position(n,k,j):
    print('shit')
    login = "Ваш логин: "+k[1::]
    returns.clear()
    logins.clear()
    locations.clear()
    returns.append(login)
    for i in db.return_installers():
        logins.append(i['login'])
    for i in logins:
        returns.append(list(db.return_location(i)))
    if j != None:
        db.insert_location(k[1::], j[0], j[1])
    return returns


if __name__ == '__main__':
    app.run_server()

