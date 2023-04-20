from dash import *
from dash_leaflet import Marker, TileLayer, Map, Tooltip
from dash.dependencies import Output, Input
import Backend.work_db as db

# Create a Dash app
app = dash.Dash(__name__)

# Define the initial marker position
logins = []
locations = []
login = "здесь ничего"
for i in db.return_installers():
        logins.append(i['login'])
for i in logins:
    locations.append(list(db.return_location(i)))
# Define a list of marker positions to loop through
markers = [TileLayer()]
for i, j in enumerate(locations):
    markers.append(Marker(id = str(i), position=list(j)))
# Define a list of marker positions to loop through


# Define the layout of the app
app.layout = html.Div([
    Map(markers, style={'width': 'auto', 'height': '50vh', 'margin': "auto", "display": "block"}, zoom=3, id= 'map'),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    ),
    html.Div(id="text"),
])

def test(l):
    global login
    login = l

# Define a callback to update the marker position

@app.callback(Output("text", "children"), [Input('interval', 'n_intervals')])

def update_marker_position(n):
    logins.clear()
    for i in db.return_installers():
        logins.append(i['login'])
    for i in logins:
        print(list(db.return_location(i)))
    return login


if __name__ == '__main__':
    app.run_server()

