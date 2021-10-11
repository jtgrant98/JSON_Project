import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile= open("US_fires_9_1.json", 'r')

fire = json.load(infile)


flames, lons, lats = [], [], []


for i in fire:
    flame = i['brightness']
    lon = i['longitude']
    lat = i['latitude']

    if flame >= 450:
        flames.append(flame)
        lons.append(lon)
        lats.append(lat)

print(flames[:5])
print(lons[:5])
print(lats[:5])


fire = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[flame % 20 for flame in flames],
        'color':flames,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':"Brightness"}}}]


my_layout = Layout(title="Fire Brightness Report 9/1 to 9/13")

fig = {'data': fire, 'layout': my_layout}

offline.plot(fig, filename="Firebrightnessreport1.html")