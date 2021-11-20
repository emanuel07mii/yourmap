import folium
import webbrowser


class Map():
    def __init__(self, lt, lg, x=15):
        self.lt = lt
        self.lg = lg
        self.x = x
        self.map = folium.Map(location=[lt, lg], zoom_start=x)

    def to_point(self, local, msg='Click aqui!', clr='red'):
        folium.Marker([self.lt, self.lg],
                      zoom_start=self.x,
                      popup=f'<i>{local}</i>',
                      tooltip=msg,
                      icon=folium.Icon(color=clr)).add_to(self.map)

    def mark_circle(self, r=50):
        folium.CircleMarker(location=(self.lt, self.lg),
                            radius=r,
                            color='#3186cc',
                            fill=True,
                            fill_color='#3186cc').add_to(self.map)

    def open_map(self, path='youmap.html'):
        html_page = f'{path}'
        self.map.add_child(folium.LatLngPopup())
        self.map.save(html_page)
        # open in browser.
        new = 2
        webbrowser.open(html_page, new=new)
