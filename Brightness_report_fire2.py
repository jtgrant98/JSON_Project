import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_14.json", 'r')
    
fire_2 = json.load(infile)


flames_2, lons_2, lats_2 = [], [], []


for i in fire_2:
    flame_2 = i['brightness']
    lon_2 = i['longitude']
    lat_2 = i['latitude']

    if flame_2 >= 450:
        flames_2.append(flame_2)
        lons_2.append(lon_2)
        lats_2.append(lat_2)

print(flames_2[:5])
print(lons_2[:5])
print(lats_2[:5])


fire_2 = [{
    'type':'scattergeo',
    'lon':lons_2,
    'lat':lats_2,
    'marker':{
        'size':[flame % 20 for flame in flames_2],
        'color':flames_2,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':"Brightness"}}}]


my_layout = Layout(title="Fire Brightness Report 9/14 to 9/21",geo_scope = 'usa')

fig = {"data": fire_2, "layout": my_layout}
offline.plot(fig, filename="Firebrightnessreport2.html")