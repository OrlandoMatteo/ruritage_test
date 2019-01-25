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

RoleModels=folium.FeatureGroup(name='Role Models').add_to(m)
Replicator=folium.FeatureGroup(name='Replicator').add_to(m)
#folium.map.Layer(name='RM').add_to(m)



folium.Marker(
    location=[5.019020, -75.621562],
    popup='Palestina',
    icon=folium.map.Icon(icon='trophy',color='lightgreen',prefix='fa')
).add_to(RoleModels)

folium.Marker(
    location=[45, -75.621562],
    popup='Replica',
    icon=folium.map.Icon(icon='leaf',color='lightgreen',prefix='fa')
).add_to(Replicator)

folium.GeoJson('palestina.json', name='Palestina boundary', tooltip='Palestina boundaries').add_to(m)

folium.map.LayerControl().add_to(m)

m.save(outfile='map.html')

class Ruritage(object):
	"""docstring for Ruritage"""
	@cherrypy.expose
	def index(self):
		page=open('map.html')
		html= """<html> 
				<body> 
					<iframe src='http://127.0.0.1:8080/map' width='1000' height='600'></iframe>
				</body> 
				</html>"""    
		#return html 
		return file('index.html')

	@cherrypy.expose
	def map(self):
		return file('map.html')

	@cherrypy.expose
	def testindex(self):
		return file('testindex.html')


config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080,
        'server.thread_pool' : 8,
        'server.max_request_body_size' : 0,
        'server.socket_timeout' : 60
    },
    '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
     '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
}

if __name__ == '__main__':
	#cherrypy.server.socket_host = '127.0.0.1' # put it here 
 	cherrypy.quickstart(Ruritage(),'/',config)