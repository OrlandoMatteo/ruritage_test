import cherrypy
import sys
import os
import csv
import random
import string
import random

import cherrypy
from os.path import abspath

import folium


m = folium.Map(location=[0,0],zoom_start=2)

#folium.map.Layer(name='RM').add_to(m)

color_dict={"Sustainable food production":"#00ff00","Pilgrimage":"#663300","Migration":"#ccccb3"}

def style_function(x):
	return {'fillcolor': color_dict[x['properties']['SIA']]}


folium.GeoJson('static/db/roleModels.json',style_function=style_function).add_to(m)

folium.map.LayerControl().add_to(m)

m.save(outfile='maps/roleModels.html')