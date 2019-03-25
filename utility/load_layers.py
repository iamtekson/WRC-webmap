import os
from django.contrib.gis.utils import LayerMapping
from .models import roadNetwork,waterPipeLine, wifiCable,wifiNode

# Auto-generated `LayerMapping` dictionary for roadNetwork model
roadnetwork_mapping = {
    'road_name': 'road_name',
    'width': 'width',
    'buffer_are': 'buffer_are',
    'type': 'type',
    'geom': 'MULTILINESTRING',
}

roadnetwork_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../data/Road_network/road_network.shp'),
)

def runRoadNetwork(verbose=True):
    lm = LayerMapping(roadNetwork, roadnetwork_shp, roadnetwork_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for waterPipeLine model
waterpipeline_mapping = {
    'diameter': 'diameter',
    'meterial': 'meterial',
    'where_from': 'Where_From',
    'towhere': 'toWhere',
    'geom': 'MULTILINESTRING',
}

waterpipeline_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../data/Water_supply/pipeline.shp'),
)

def runWaterPipeLine(verbose=True):
    lm = LayerMapping(waterPipeLine, waterpipeline_shp, waterpipeline_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for wifiCable model
wificable_mapping = {
    'core': 'core',
    'mbps': 'mbps',
    'from_field': 'from_',
    'to': 'to',
    'geom': 'MULTILINESTRING',
}

wificable_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../data/wifi_network/wifi_cable.shp'),
)

def runWifiCable(verbose=True):
    lm = LayerMapping(wifiCable, wificable_shp, wificable_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


# Auto-generated `LayerMapping` dictionary for wifiNode model
wifinode_mapping = {
    'router_poi': 'Router_poi',
    'geom': 'MULTIPOINT',
}

wifinodes_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../data/wifi_network/nodes.shp'),
)

def runWifiNode(verbose=True):
    lm = LayerMapping(wifiNode, wifinodes_shp, wifinode_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
