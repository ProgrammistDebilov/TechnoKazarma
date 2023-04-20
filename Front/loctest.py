import dash
from dash import html
from dash_leaflet import Marker, TileLayer, Map, Tooltip
from dash import dcc
from dash.dependencies import Output, Input
import random
import Backend.work_db as db

# Create a Dash app
app = dash.Dash(__name__)

# Define the initial marker position
logins = []
locations = []
login = ""
for i in db.return_installers():
        logins.append(i['login'])
for i in logins:
    locations.append(list(db.return_location(i)))
# Define a list of marker positions to loop through
markers = [TileLayer()]
for i, j in enumerate(locations):
    markers.append(Marker(id = str(i), position=list(j)))

print(markers)
# Define a list of marker positions to loop through


# Define the layout of the app
app.layout = html.Div([
    Map(markers, style={'width': 'auto', 'height': '98vh', 'margin': "auto", "display": "block"}, zoom=3),
    html.Div(id="text"),
    dcc.Interval(
        id='interval',
        interval=2000, # Refresh every 2 seconds
        n_intervals=0
    )
])

def test(l):
    global login
    login = l

# Define a callback to update the marker position

@app.callback(Output('marker', 'position'),Output('marker2', 'position'), Output('text', 'children'), [Input('interval', 'n_intervals'), Input('marker', 'children'), Input('marker2', 'children')])
def update_marker_position(n, k, j):
    print(k['props']['children'], j['props']['children'])
    logins.clear()
    for i in db.return_installers():
        logins.append(i['login'])
    for i in logins:
        print(list(db.return_location(i)))
    return [[str(random.randint(-90,90)), str(random.randint(-180,180))],[random.randint(-90,90), random.randint(-180,180)], login]



if __name__ == '__main__':
    app.run_server()

