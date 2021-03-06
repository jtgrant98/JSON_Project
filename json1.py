import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]

mags = []
lons = []
lats = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    long = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags)
print(lons)
print(lats)

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquake 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='globalearthquake1day.html')




