from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('point_dataset', views.point_dataset, name = 'point_dataset'),
	path('road_dataset', views.road_dataset, name = 'road_dataset'),
	path('wifi_dataset', views.wifi_dataset, name= 'wifi_dataset'),
	path('wifi_node', views.wifi_node, name= 'wifi_node')

]