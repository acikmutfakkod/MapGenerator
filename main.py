import folium as fo

# Haritayı görüntülemek
class FindPlace():

    def __init__(self):
        # Map() sınıfının örneğini (instance) oluşturur
        self.fo_map = fo.Map()  #openstreetmap #Mapbox Bright #stamenterrain #stamentoner #stamenwatercolor #cartodbpositron #CartoDB dark_matter
        # FeatureGroup() sınıfının örneğini (instance) oluşturur
        self.fgi = fo.FeatureGroup(name='OpenStreetMap')
        self.x = 0.0
        self.y = 0.0

        self.run()
        self.show_map()

    def mark_coordinates(self, x, y):
        # FeatureGroup() sınıfının add_child() metoduna instance üzerinden erişerek harita üzerinde koordinatları verilen lokasyon işaretlenir
        self.fgi.add_child(fo.Marker(location=[x, y], popup='varış yeri', icon=fo.Icon(color='red')))
        self.fo_map.add_child(self.fgi)

    def show_map(self):
        self.fo_map.save('map.html')

    def run(self):
        self.x = float(input('İlk koordinatı girin: '))
        self.y = float(input('İkinci koordinatı girin: '))
        self.mark_coordinates(self.x, self.y)

if __name__ == '__main__':
    fp = FindPlace()

