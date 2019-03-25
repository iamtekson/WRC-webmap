from django.contrib import admin
from .models import points, roadNetwork, waterPipeLine, wifiCable, wifiNode
from leaflet.admin import LeafletGeoAdmin


class pointsAdmin(LeafletGeoAdmin):
	list_display = ('title', 'location')

class roadNetworkAdmin(LeafletGeoAdmin):
	list_display = ('id','road_name', 'type','width','buffer_are')
	list_display_links = ('id', 'road_name')
	list_filter = ('road_name',)
	search_filelds = ('id','road_name', 'type','width','buffer_are')
	list_per_page = 25

class waterPipeLineAdmin(LeafletGeoAdmin):
	list_display = ('where_from', 'towhere')

class wifiCableAdmin(LeafletGeoAdmin):
	list_display = ('from_field', 'to')

class wifiNodeAdmin(LeafletGeoAdmin):
	list_display = ('id', 'geom')

admin.site.register(points, pointsAdmin)
admin.site.register(roadNetwork, roadNetworkAdmin)
admin.site.register(waterPipeLine, waterPipeLineAdmin)
admin.site.register(wifiCable, wifiCableAdmin)
admin.site.register(wifiNode, wifiNodeAdmin)