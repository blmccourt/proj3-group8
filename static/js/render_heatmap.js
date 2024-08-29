function getColor(value) {
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

// define mouseover and popup behavior
function onEachFeatureFn(feature, layer) {
    if (feature.properties && feature.properties.country) {
        const formatted_prevalence = feature.properties.prevalence.toFixed(1) + "%"

        var popupContent = `
            <div style="text-align: center">
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

var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 4,
}).addTo(map);

// define variable to store current layer
var currentGeoJsonLayer;

// set overweight layer as default
loadGeoJson(overweight_layer_geojson_data_gdf)

// function called to reload GeoJSON data upon select menu usage
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

document.getElementById('geojson-select').addEventListener('change', function(event) {

    var selection = event.target.value;

    // depending on selection, load the appropriate data onto the map as a layer
    if (selection == "overweight") {
        loadGeoJson(overweight_layer_geojson_data_gdf)
    } else if (selection == "stunting") {
        loadGeoJson(stunting_layer_geojson_data_gdf)
    } else if (selection == "underweight") {
        loadGeoJson(underweight_layer_geojson_data_gdf)
    } else if (selection == "wasting") {
        loadGeoJson(wasting_layer_geojson_data_gdf)
    } else if (selection == "wasting_severe") {
        loadGeoJson(wasting_severe_layer_geojson_data_gdf)
    } else {
        console.log("invalid selection!");
    }
});
