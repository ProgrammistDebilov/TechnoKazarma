import folium
import webbrowser

m = folium.Map()
m.save("map.html")
webbrowser.open("map.html")