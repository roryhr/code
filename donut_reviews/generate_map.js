// Link to data on Github??
// donutShop = $.getJSON("donut_data.json")


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

    var numberList = document.getElementById("listings");

    var newNumberListItem = document.createElement("li");

    // //create new text node
    var numberListValue = document.createTextNode(feature.properties.popupContent);

    //add text node to li element
    newNumberListItem.appendChild(numberListValue);

    //add new list element built in previous steps to unordered list
    //called numberList
    numberList.appendChild(newNumberListItem);
    
    // var theDiv = document.getElementById("listings");
    // var content = document.createTextNode(feature.properties.popupContent);
    // theDiv.appendChild(content);
}

L.geoJSON(donutShop, {
    onEachFeature: onEachFeature
}).addTo(map);
