---
layout: minimal
---

<!DOCTYPE html>
<html>
<head>

  <meta charset=utf-8 />

  <title>Waste Facility Map</title>

    <!-- D3.js -->
    <script src="http://d3js.org/d3.v3.min.js"></script>

    <!-- MAPBOX-gl -->
    <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.31.0/mapbox-gl.js'></script>
    <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.31.0/mapbox-gl.css' rel='stylesheet' />

    <!-- STYLES -->
    <link rel="stylesheet" type="text/css" href="/css/map.css">
    <link rel="stylesheet" type="text/css" href="/css/popup.css">
    <link rel="stylesheet" type="text/css" href="/css/marker.css">

    <!-- FONTS -->
    <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700' rel='stylesheet'>


</head>

<body>

<div class='sidebar'>
  <div class='heading'>
    <h1>Waste Facility Listing</h1>
  </div>
  <div id='listings' class='listings'></div>
</div>


<div id='map' class='map pad2'>Map</div>


<script>

// This will let you use the .remove() function later on
if (!('remove' in Element.prototype)) {
  Element.prototype.remove = function() {
    if (this.parentNode) {
      this.parentNode.removeChild(this);
    }
  };
}


// initialize the map
mapboxgl.accessToken = 'pk.eyJ1IjoiZXN0YW1ib2xpZXZhIiwiYSI6ImNpeXZudHB3czAwMjcyd21zcHFidjZ2eWUifQ.fMIEvI7LPrICPLuf8RJ4xA';

var map = new mapboxgl.Map({
  // container id specified in the HTML
  container: 'map',
  // style URL
  style: 'mapbox://styles/mapbox/light-v9',
  // initial position in [long, lat] format
  center: [-77.034084, 38.909671],
  // initial zoom
  zoom: 14
});


d3.json("/data/sweetgreen.geojson", function(facilities)
{
  console.log(facilities);

  map.on('load', function(e) {
  // Add the data to your map as a layer
  map.addSource('places', {
    type: 'geojson',
    data: facilities
  });

  facilities.features.forEach(function(marker) {
    // Create a div element for the marker
    var el = document.createElement('div');
    // Add a class called 'marker' to each div
    el.className = 'marker';
    // By default the image for your custom marker will be anchored
    // by its top left corner. Adjust the position accordingly
    el.style.left = '-28px';
    el.style.top = '-46px';
    // Create the custom markers, set their position, and add to map
    new mapboxgl.Marker(el)
      .setLngLat(marker.geometry.coordinates)
      .addTo(map);

    // add a listener
    el.addEventListener('click', function(e) {
      var activeItem = document.getElementsByClassName('active');
      // 1. Fly to the point
      flyToFacility(marker);
      // 2. Close all other popups and display popup for clicked store
      createPopUp(marker);
      // 3. Highlight listing in sidebar (and remove highlight for all other listings)
      e.stopPropagation();
      if (activeItem[0]) {
        activeItem[0].classList.remove('active');
      }
      var listing = document.getElementById('listing-' + i);
      console.log(listing);
      listing.classList.add('active');
    });

  });

  buildLocationList(facilities);

  // listen for a click on the map

  });

});

// function to iterate over all locations
function buildLocationList(data) {
  // Iterate through the list of stores
  for (i = 0; i < data.features.length; i++) {
    var currentFeature = data.features[i];
    // Shorten data.feature.properties to just `prop` so we're not
    // writing this long form over and over again.
    var prop = currentFeature.properties;
    // Select the listing container in the HTML and append a div
    // with the class 'item' for each store
    var listings = document.getElementById('listings');
    var listing = listings.appendChild(document.createElement('div'));
    listing.className = 'item';
    listing.id = 'listing-' + i;

    // Create a new link with the class 'title' for each store
    // and fill it with the store address
    var link = listing.appendChild(document.createElement('a'));
    link.href = '#';
    link.className = 'title';
    link.dataPosition = i;
    link.innerHTML = prop.address;

    // Create a new div with the class 'details' for each store
    // and fill it with the city and phone number
    var details = listing.appendChild(document.createElement('div'));
    details.innerHTML = prop.city;
    if (prop.phone) {
      details.innerHTML += ' &middot; ' + prop.phoneFormatted;
    }

    // Add an event listener for the links in the sidebar listing
    link.addEventListener('click', function(e) {
      console.log(e);
      // Update the currentFeature to the store associated with the clicked link
      var clickedListing = data.features[this.dataPosition];
      // 1. Fly to the point associated with the clicked link
      flyToFacility(clickedListing);
      // 2. Close all other popups and display popup for clicked store
      createPopUp(clickedListing);
      // 3. Highlight listing in sidebar (and remove highlight for all other listings)
      var activeItem = document.getElementsByClassName('active');
      if (activeItem[0]) {
        activeItem[0].classList.remove('active');
      }
      this.parentNode.classList.add('active');
    });


  }
}

// fly map to location
function flyToFacility(currentFeature) {
  map.flyTo({
    center: currentFeature.geometry.coordinates,
    zoom: 15
  });
}

//  build a pop=up
function createPopUp(currentFeature) {
  var popUps = document.getElementsByClassName('mapboxgl-popup');
  // Check if there is already a popup on the map and if so, remove it
  if (popUps[0]) popUps[0].remove();

  var popup = new mapboxgl.Popup({ closeOnClick: false })
    .setLngLat(currentFeature.geometry.coordinates)
    .setHTML('<h3>Sweetgreen</h3>' +
      '<h4>' + currentFeature.properties.address + '</h4>')
    .addTo(map);
}






</script>

</body>

</html>
