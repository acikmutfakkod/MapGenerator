import folium as fo

# Haritayı görüntülemek
fo_map = fo.Map(location=[39.931774, 32.838673], zoom_start=13, tiles='openstreetmap')  #openstreetmap #Mapbox Bright #stamenterrain #stamentoner #stamenwatercolor #cartodbpositron #CartoDB dark_matter

fo_map.save('map.html')
