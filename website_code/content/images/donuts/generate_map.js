// Link to data on Github??
// donutShop = $.getJSON("donut_map.json")


var map = L.map('map').setView([37.28099, -121.95252], 9);

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

L.geoJSON(donutShop, {
    onEachFeature: onEachFeature
}).addTo(map);


function generateCardGroup() {
    // Not used. Rendering Cards with Python/Jinja2. Maybe later
    var donutGroup = document.getElementById("donutimages");

    var cardContainer = document.createElement("div");
    cardContainer.className = "col mb-4";

    var card = document.createElement("div");
    card.className = "card";

    var cardBody = document.createElement("div");
    cardBody.className = "card-body";
    
    var cardTitle = document.createElement("h5");
    cardTitle.className = "card-title";
    cardTitle.textContent = "Donut Shop Name";

    var cardText = document.createElement("p");
    
    cardText.className = "card-text";
    cardText.textContent = "Some review text goes here";

    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardText);

    card.appendChild(cardBody);

    cardContainer.appendChild(card);
    donutGroup.appendChild(cardContainer);
}

