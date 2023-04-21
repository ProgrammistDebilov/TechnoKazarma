from dash import *
from dash_leaflet import TileLayer, Map, LocateControl, Marker, Tooltip, Popup
from dash.dependencies import Output, Input
import Backend.work_db as db
from geopy.geocoders import GeoNames
# Create a Dash app
app = dash.Dash(__name__)
# define icons
icon_green = {
    "iconUrl": 'https://i.ibb.co/SmZPXPc/25962fdc-4e92-4303-97c6-ea2c7e52d4cc.png',
    "iconSize": [32, 48],  # size of the icon
    "iconAnchor": [16,48]
}
icon_red = {
    "iconUrl": 'https://i.ibb.co/dKP3Lm5/2c4a6b06-72cd-49e1-950d-ec2d5295d9b5.png',
    "iconSize": [32, 48],  # size of the icon
    "iconAnchor": [16,48]
}
icon_yellow = {
    "iconUrl": 'https://i.ibb.co/zfvg2jM/f18848bd-2052-47cd-9679-8651bd705346.png',
    "iconSize": [32, 48],  # size of the icon
    "iconAnchor": [16,48]
}
icon_blue = {
    "iconUrl": 'https://i.ibb.co/cLc0LqR/5a4e9025-e5d4-4696-93c1-219f3821567d.png',
    "iconSize": [32, 48],  # size of the icon
    "iconAnchor": [16,48]
}
icon_black = {
    "iconUrl": 'https://i.ibb.co/LCKQHFQ/5c3434f1-6dcf-4577-b47b-2c448ccfd56d.png',
    "iconSize": [32, 48],  # size of the icon
    "iconAnchor": [16,48]
}
installers_icons = {
    "1": icon_black,
    "0": icon_red
}
orders_icons = {
    "-1": icon_blue,
    "0": icon_yellow,
    "1": icon_green
}
#define geolocator
geolocator = GeoNames(username="null_geodata" ,user_agent="MyApp")

# Define the layout of the app
app = Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)
app.layout = html.Div([
    Map( style={'width': 'auto', 'height': '95vh', 'margin': "auto", "display": "block"}, zoom=3, id= 'map'),
    dcc.Interval(
        id='interval',
        interval=2500, # Refresh every 2.5 seconds
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
    markers = [TileLayer(), LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})]
    login = k[1::]
    name_login = "Ваш логин: " + login
    if j != None:
        db.insert_location(login, j[0], j[1])
    for i,j in enumerate(db.return_installers()):
        markers.append(Marker(id = str(i), icon=installers_icons[str(j['alacrity'])], position=db.return_location(j['login']), children=[Tooltip(j['login']),Popup([html.Div("Инсталятор: "+j['login']), html.Div("Рейтинг: "+str(j['rating']))])]))
        max_num = i
    for i,j in enumerate(db.return_orders()):
        try:
            location = geolocator.geocode(j['adress'])
        except ConnectionError:
            location = None
        k = max_num + i + 1
        if location != None:
            match j['state']:
                case 1:
                    markers.append(Marker(id = str(k), icon = orders_icons[str(j['state'])], position = [location.latitude, location.longitude], children=[Tooltip(location.address), Popup([html.Div("Адрес: "+location.address), html.Div("Исполнитель: "+ str(j['installer'])), html.Div("Комментарий: "+j['comment'])])]))
                case 0:
                    markers.append(Marker(id = str(k), icon = orders_icons[str(j['state'])], position = [location.latitude, location.longitude], children=[Tooltip(location.address), Popup([html.Div("Адрес: "+location.address), html.Div("Исполнитель: "+ str(j['installer']))])]))
                case -1:
                    markers.append(Marker(id = str(k), icon = orders_icons[str(j['state'])], position = [location.latitude, location.longitude], children=[Tooltip(location.address), Popup([html.Div("Адрес: "+location.address)])]))
    return [markers,name_login]


if __name__ == '__main__':
    app.run_server()

