import os
import folium
import json
import pandas as pd
from branca.colormap import linear

###

#state_data = pd.read_csv(US_Unemployment_Oct2012)

#m = folium.Map(location=[48, -102], zoom_start=3)
#m.choropleth(
#    geo_data=geo_json_data,
#    data=count_dict,
    #columns=['State', 'Unemployment'],
#    key_on='feature.properties.name',
#    fill_color='YlGn',
#    fill_opacity=0.7,
#    line_opacity=0.2,
#    legend_name='Unemployment Rate (%)',
#    highlight=True
#)

#m.save(os.path.join('results', 'GeoJSON_and_choropleth_11.html'))

#m

###

#US_Unemployment_Oct2012 = os.path.join('data', 'US_Unemployment_Oct2012.csv')
#unemployment = pd.read_csv(US_Unemployment_Oct2012)

count_dict = {'Charlotte County': 5, 'Seminole County': 3} #unemployment.set_index('State')['Unemployment']

colormap = linear.YlGn.scale(min(count_dict.values()), max(count_dict.values()))

###
us_states = os.path.join('data', 'fl_counties.json')

geo_json_data = json.load(open(us_states))

m = folium.Map([27.6648, -83.5158], zoom_start=6)

folium.GeoJson(
    geo_json_data,
    name='unemployment',
    #legend_name='Unemployment Rate (%)',
    #highlight=True,
    #fill_color='YlGn',
    style_function=lambda feature: {
        'fillColor': colormap(count_dict.get(feature['properties']['name'], 0)),
        'color': 'black',
        'weight': 1,
        'dashArray': '5, 5',
        'fillOpacity': 0.9,
    }
).add_to(m)

#m.choropleth(
#    geo_json_data,
#    fill_color='YlGn',
#    fill_opacity=0.7,
#    line_opacity=0.2,
#    legend_name='Unemployment Rate (%)',
    #highlight=True
#)

folium.LayerControl().add_to(m)

#for idx, row in geo_json_data.items():
#    popup = idx
#    folium.CircleMarker([row['latitude'], row['longitude']], popup=popup,
#                        radius=1, color='white').add_to(map)

###
'''

folium.GeoJson(geo_json_data).add_to(m)
'''
m.save(os.path.join('results', 'GeoJSON_and_choropleth_0.html'))
m
