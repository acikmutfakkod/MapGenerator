import folium as fo

# Haritayı görüntülemek
# Map() sınıfının örneğini (instance) oluşturur
fo_map = fo.Map()  #openstreetmap #Mapbox Bright #stamenterrain #stamentoner #stamenwatercolor #cartodbpositron #CartoDB dark_matter
# FeatureGroup() sınıfının örneğini (instance) oluşturur
fgi = fo.FeatureGroup(name='OpenStreetMap')
# FeatureGroup() sınıfının add_child() metoduna instance üzerinden erişerek harita üzerinde koordinatları verilen lokasyon işaretlenir
fgi.add_child(fo.Marker(location=[39.931774, 32.838673], popup='varış yeri', icon=fo.Icon(color='red')))
fo_map.add_child(fgi)


fo_map.save('map.html')
