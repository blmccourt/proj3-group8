/*
var map = L.map('map').setView([51.505, -0.09], 13);

// Set up the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

// GeoJSON Layer 1
var geojsonData1 = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-0.09, 51.505]
            }
        },
        // Add more points as needed
    ]
};

// GeoJSON Layer 2
var geojsonData2 = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-0.1, 51.515]
            }
        },
        // Add more points as needed
    ]
};

// Extract coordinates from GeoJSON 1
var heatData1 = geojsonData1.features.map(function(feature) {
    return [feature.geometry.coordinates[1], feature.geometry.coordinates[0]];
});

// Extract coordinates from GeoJSON 2
var heatData2 = geojsonData2.features.map(function(feature) {
    return [feature.geometry.coordinates[1], feature.geometry.coordinates[0]];
});

// Create heatmap layer for Layer 1
var heatLayer1 = L.heatLayer(heatData1, {
    radius: 25,
    blur: 0,
    maxZoom: 17,
    gradient: {0.4: 'blue', 0.65: 'lime', 1: 'red'} // Custom gradient for layer 1
});

// Create heatmap layer for Layer 2
var heatLayer2 = L.heatLayer(heatData2, {
    radius: 25,
    blur: 0,
    maxZoom: 17,
    gradient: {0.4: 'purple', 0.65: 'orange', 1: 'yellow'} // Custom gradient for layer 2
});

// Add layers to the map
heatLayer1.addTo(map);
heatLayer2.addTo(map);

// Layer control to toggle between layers
var baseLayers = {};
var overlayLayers = {
    "Heatmap Layer 1": heatLayer1,
    "Heatmap Layer 2": heatLayer2
};

L.control.layers(baseLayers, overlayLayers).addTo(map);
*/

//console.log("test")

function getColor(value) {
    //console.log("in getColor")
    return value > 30 ? '#FF0000' :
           value > 20 ? '#FFA500' :
           value > 10 ? '#FFFF00' :
                        '#00FF00';
}

function style(feature) {
    return {
        color: getColor(feature.properties.prevalence),
        radius: 5,
        weight: 2
    };
}

function onEachFeatureFn(feature, layer) {
    if (feature.properties && feature.properties.country) {
        //console.log("here")
        const formatted_prevalence = feature.properties.prevalence.toFixed(1) + "%"

        var popupContent = `
            <div style="text-align: center;">
                <h3>${feature.properties.country}</h3>
                <p><strong>${formatted_prevalence}</strong></p>
            </div>
        `;
        layer.bindPopup(popupContent);
    }

    layer.on({
        mouseover: function(e) {
            var layer = e.target;
            layer.openPopup();
        },
        mouseout: function(e) {
            var layer = e.target;
            layer.closePopup();
        }
    });
}

function loadGeoJson(selected_dataset) {
    if(currentGeoJsonLayer) {
        map.removeLayer(currentGeoJsonLayer);
    }

    currentGeoJsonLayer = L.geoJSON(selected_dataset, {

        onEachFeature: onEachFeatureFn,
        pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng, style(feature));
        }

    }).addTo(map);

    map.fitBounds(L.geoJSON(selected_dataset).getBounds());
}

var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 4,
}).addTo(map);


// set default layer to display (overweight)
var currentGeoJsonLayer;
/*
var geoJsonLayerOverweight = L.geoJSON(overweight_layer_geojson_data)
var geoJsonLayerStunting = L.geoJSON(stunting_layer_geojson_data)
var geoJsonLayerUnderweight = L.geoJSON(underweight_layer_geojson_data)
var geoJsonLayerWasting = L.geoJSON(wasting_layer_geojson_data)
var geoJsonLayerWastingSevere = L.geoJSON(wasting_severe_layer_geojson_data)
*/
loadGeoJson(overweight_layer_geojson_data)

document.getElementById('geojson-select').addEventListener('change', function(event) {
    //console.log(event.target.value);
    var selection = event.target.value;
    //loadGeoJson(selection);

    // depending on selection, load the appropriate data onto the map as a layer

    if (selection == "overweight_layer_geojson_data") {
        loadGeoJson(overweight_layer_geojson_data)
    } else if (selection == "stunting_layer_geojson_data") {
        loadGeoJson(stunting_layer_geojson_data)
    } else if (selection == "underweight_layer_geojson_data") {
        loadGeoJson(underweight_layer_geojson_data)
    } else if (selection == "wasting_layer_geojson_data") {
        loadGeoJson(wasting_layer_geojson_data)
    } else if (selection == "wasting_severe_layer_geojson_data") {
        loadGeoJson(wasting_severe_layer_geojson_data)
    } else {
        console.log("invalid selection!");
    }
});
/*
var geojsonLayer = new L.GeoJSON.AJAX("./data/overweight_layer.geojson");
geojsonLayer.addTo(map)

fetch('./data/overweight_layer.geojson')
    .then(response => response.json())
    .then(data => {
        var geojsonLayer = L.geoJSON(data).addTo(map);

        // Optional: Fit the map view to the bounds of the GeoJSON layer
        map.fitBounds(geojsonLayer.getBounds());
        console.log("created layer")
    })
    .catch(error => console.log("error loading geojson file:", error));
*/

