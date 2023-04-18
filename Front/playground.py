import folium
import webbrowser

m = folium.Map(zoom_control=200)

m.save("a.html")
webbrowser.open("a.html")