from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import points, roadNetwork, wifiCable,wifiNode

def index(request):
	return render(request, 'index.html')

def point_dataset(request):
	p = serialize('geojson', points.objects.all())
	return HttpResponse(p,content_type='json')

def road_dataset(request):
	r = serialize('geojson', roadNetwork.objects.all())
	return HttpResponse(r,content_type='json')

def wifi_dataset(request):
	wifi = serialize('geojson', wifiCable.objects.all())
	return HttpResponse(wifi, content_type='json')

def wifi_node(request):
	wifi_node = serialize('geojson', wifiNode.objects.all())
	return HttpResponse(wifi_node, content_type= 'json')