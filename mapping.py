import folium
import json
import locale
from folium import IFrame

def get_browser_language():
    try:
        locale.setlocale(locale.LC_ALL, '')
        lang = locale.getlocale()[0]
        if lang and lang.startswith("es"):
            return "es"
    except:
        pass
    return "en"

lang = get_browser_language()

with open("data/data.json", encoding="utf-8") as f:
    data = json.load(f)

map = folium.Map(location=[9.75, -84], zoom_start=7)

fg_volc = folium.FeatureGroup(name="Volcanoes")
for volc in data["volcanoes"]:
    name = volc["name"].get(lang, volc["name"]["en"])
    elevation = volc["elevation"]
    url = volc["url"]
    status = volc["status"]
    volclocation = volc["location"]
    popup_html = f"""
        <b>{name}</b><br>
        🌋 {elevation} m — {status}<br>
        📍 {volclocation}<br>
        <a href="{url}" target="_blank">More info</a>
        """
    iframe = IFrame(html=popup_html, width=200, height=80)
    fg_volc.add_child(folium.Marker(
        location=[volc["lat"], volc["lon"]],
        popup=folium.Popup(iframe),
        icon=folium.CustomIcon('icons/volcan_icon.png', icon_size=(30, 30))
    ))

fg_air = folium.FeatureGroup(name="Airports")
for air in data["airports"]:
    name = air["name"].get(lang, air["name"]["en"])
    type_ = air["type"].get(lang, air["type"]["en"])
    airlocation = air["location"]
    popup_html = f"✈️ <b>{name}</b><br>{type_} Airport <br> 📍 { airlocation}"
    iframe = IFrame(html=popup_html, width=200, height=80)
    fg_air.add_child(folium.Marker(
        location=[air["lat"], air["lon"]],
        popup=folium.Popup(iframe),
        icon=folium.CustomIcon('icons/airport.png', icon_size=(30, 30))
    ))

fg_aero = folium.FeatureGroup(name="Aeródromos")
for aero in data.get("aerodromes", []):
    name = aero["name"].get(lang, aero["name"]["en"])
    type_ = aero["type"].get(lang, aero["type"]["en"])
    lat = aero["lat"]
    lon = aero["lon"]
    aerolocation = aero["location"]
    
    if lat is None or lon is None:
        continue
    
    popup_html = f"🛩️ <b>{name}</b><br>{type_} Aerodrome <br> 📍 { aerolocation} "
    iframe = folium.IFrame(html=popup_html, width=200, height=80)
    
    fg_aero.add_child(folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(iframe),
        icon=folium.CustomIcon('icons/aerodrome.png', icon_size=(30, 30))
    ))

map.add_child(fg_volc)
map.add_child(fg_air)
map.add_child(fg_aero)
map.add_child(folium.LayerControl())
map.save("output/map.html")