/* ====================
 Adding  Multiple tile layers
==================== */
var osmLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>',
	thunLink = '<a href="http://thunderforest.com/">Thunderforest</a>';

var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	osmAttrib = '&copy; ' + osmLink + ' Contributors',
	landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
	thunAttrib = '&copy; '+osmLink+' Contributors & '+thunLink;

var osmMap = L.tileLayer(osmUrl, {attribution: osmAttrib}),
	landMap = L.tileLayer(landUrl, {attribution: thunAttrib});

var map = L.map('gis', {
	layers:[osmMap]}).setView([28.2539, 83.9764], 17);

var baseLayers = {
	"OSM Mapnik": osmMap,
	"Landscape": landMap
	};

// L.control.layers(baseLayers).addTo(map);

/* =============================================================================
 				Overlaying Information Interactively on Map
============================================================================== */
var coolPlaces = new L.LayerGroup();

		L.marker([28.2539, 83.9764])
		.bindPopup('Te Papa').addTo(coolPlaces),
		L.marker([-41.29437, 174.78405])
		.bindPopup('Embassy Theatre').addTo(coolPlaces),
		L.marker([-41.2895, 174.77803])
		.bindPopup('Michael Fowler Centre').addTo(coolPlaces),
		L.marker([-41.28313, 174.77736])
		.bindPopup('Leuven Belgin Beer Cafe').addTo(coolPlaces),

		L.polyline([
		[28.2539, 83.9764],
		[-41.2895, 174.77803],
		[-41.29042, 174.78219],
		[-41.29437, 174.78405]
		]
		).addTo(coolPlaces);

		



/* =============================================================================
							Add Required Geojson Files
============================================================================== */
/*var geojsonLayer = new L.GeoJSON.AJAX("data/geojson/roadNetwork.geojson");       
geojsonLayer.addTo(map);*/


 var points = new L.LayerGroup();
 $.getJSON("{% url 'point_dataset' %}", function(data) {
    var geojson = L.geoJson(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.road_name);
      }
    });
geojson.addTo(points);
    });
 var overlays = {
		"Interesting places": coolPlaces,
		"Important Places": points
		};
L.control.layers(baseLayers,overlays).addTo(map);
L.control.scale().addTo(map);

/* =============================================================================
							Add Shapefile Option
============================================================================== */
document.getElementById("submit").onclick = function(e){
	var files = document.getElementById('file').files;
	if (files.length == 0) {
	  return; //do nothing if no file given yet
  }
  
  var file = files[0];
  
  if (file.name.slice(-3) != 'zip'){ //Demo only tested for .zip. All others, return.
		document.getElementById('warning').innerHTML = 'Select .zip file';  	
    return;
  } else {
  	document.getElementById('warning').innerHTML = ''; //clear warning message.
    handleZipFile(file);
  }
};

//More info: https://developer.mozilla.org/en-US/docs/Web/API/FileReader
function handleZipFile(file){
	var reader = new FileReader();
  reader.onload = function(){
	  if (reader.readyState != 2 || reader.error){
		  return;
	  } else {
		  convertToLayer(reader.result);
  	}
  }
  reader.readAsArrayBuffer(file);
}

function convertToLayer(buffer){
	shp(buffer).then(function(geojson){	//More info: https://github.com/calvinmetcalf/shapefile-js
    var layer = L.shapefile(geojson).addTo(map);//More info: https://github.com/calvinmetcalf/leaflet.shapefile
    console.log(layer);
  });
}