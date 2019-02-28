
import folium
import pandas

travel_file_data = pandas.read_csv("places_traveled.csv")

latitude = list(travel_file_data["Lat"])
longitude = list(travel_file_data["Lon"])
city = list(travel_file_data["City"])
ID = list(travel_file_data["ID"])
country = list(travel_file_data["Country"])


def style_func(data):
        if data["properties"]["NAME"] in country:
            return {"fillColor": "green"}
        else:
            return {"fillColor": "blue"}


travel_map = folium.Map(location=[51.533157, -0.127676], zoom_start=6)
fg_travel_loc = folium.FeatureGroup(name="travel locations")
fg_country_info = folium.FeatureGroup(name="country information")


for id in ID:
    for lat, lon, cit in zip(latitude, longitude, city):
        fg_travel_loc.add_child(folium.Marker(location=[lat, lon], popup=cit))

fg_country_info.add_child(folium.GeoJson(data=open("world.json", encoding="utf-8-sig").read(),
                                         style_function=style_func))


travel_map.add_child(fg_travel_loc)
travel_map.add_child(fg_country_info)
travel_map.save("hr_travel.html")

