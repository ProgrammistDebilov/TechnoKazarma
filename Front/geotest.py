# Import the required library
from geopy.geocoders import Nominatim
import folium
from folium import plugins, branca
import webbrowser
import random

m = folium.Map(zoom_control=200)



# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

geolocation = "Южно-Сахалинск Комсомольская 277"

location = geolocator.geocode(geolocation)
print(location)
randomdata= []

for i in range(100000):
    randomdata.append((random.randint(-90.000000000,90.000000000),random.randint(-720.000000000,720.000000000)))

#longatt= str(location.latitude)+","+str(location.longitude)
plugins.HeatMap(randomdata, radius=10, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'red'}).add_to(m)
colormap = branca.colormap.LinearColormap(['blue', 'lime', 'red'], 
                                          vmin=1, 
                                          vmax=5, 
                                          caption='Нарастание загруженности')
colormap.add_to(m)
m.save("a.html")
webbrowser.open("a.html")