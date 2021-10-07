import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

with open("US_fires_9_1.json") as data_file:
    fire = json.load(data_file)


flames, longs, lats = [], [], []


for i in fire:
    flame = i['brightness']
    long = i['longitude']
    lat = i['latitude']

    if flame >= 450:
        flames.append(flame)
        longs.append(long)
        lats.append(lat)

print(flames[:5])
print(longs[:5])
print(lats[:5])


fire = [{
    'type':'scattergeo',
    'long':'longs',
    'lat':'lats',
    'marker':{
        'size':[flame % 5 for flame in flames],
        'color':flames,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':"Brightness"}}}]


my_layout = Layout(title="Fire Brightness Report 9/1 to 9/13")

fig = {"Data": fire, "Layout": my_layout}
offline.plot(fig, filename="Firebrightnessreport1.html")