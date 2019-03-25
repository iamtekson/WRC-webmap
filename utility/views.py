from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import points, roadNetwork

def index(request):
	return render(request, 'index.html')

def point_dataset(request):
	p = serialize('geojson', points.objects.all())
	return HttpResponse(p,content_type='json')

def road_dataset(request):
	p = serialize('geojson', roadNetwork.objects.all())
	return HttpResponse(p,content_type='json')

