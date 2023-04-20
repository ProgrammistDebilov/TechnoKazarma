from dash import *
from dash_leaflet import Marker, TileLayer, Map, Tooltip, LocateControl
from dash.dependencies import Output, Input
import Backend.work_db as db

# Create a Dash app
app = dash.Dash(__name__)


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

for i in range(len(logins)):
    callbacks.append(Output(str(i), "position"))
print(callbacks)
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
        print(j[0], j[1])
        print(logins)
        print(returns)
        print(locations)
    return returns


if __name__ == '__main__':
    app.run_server()

