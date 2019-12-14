// Link to data on Github??
// donutShop = $.getJSON("donut_data.json")
// Link to data on Github??

var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var donutShop = JSON.parse(this.responseText);

        L.geoJSON(donutShop, {
            onEachFeature: onEachFeature
        }).addTo(map);
    }
};


var map = L.map('map').setView([37.28099, -121.95252], 7);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox.light'
}).addTo(map);

function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}

xmlhttp.open("GET", url="https://raw.githubusercontent.com/roryhr/code/master/donut_reviews/output/map_data.json", async=true);
xmlhttp.send();
