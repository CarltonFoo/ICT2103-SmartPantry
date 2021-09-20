<!DOCTYPE html>
<html lang="en">
    <head>
        <title>SmartTrip</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <?php
        include "header.php";
        ?>
    </head>
    <body>
        <?php
        include "nav.php";
        ?>
        
        <div id='mapdiv'></div>

        <script>
            var center = L.bounds([1.56073, 104.11475], [1.16, 103.502]).getCenter();
            var map = L.map('mapdiv').setView([center.x, center.y], 12);

            var basemap = L.tileLayer('https://maps-{s}.onemap.sg/v3/Default/{z}/{x}/{y}.png', {
                detectRetina: true,
                maxZoom: 18,
                minZoom: 11
            });

            map.setMaxBounds([[1.56073, 104.1147], [1.16, 103.502]]);

            basemap.addTo(map);

            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                }
            }

            function showPosition(position) {
                marker = new L.Marker([position.coords.latitude, position.coords.longitude], {bounceOnAdd: false}).addTo(map);
                var popup = L.popup()
                        .setLatLng([position.coords.latitude, position.coords.longitude])
                        .setContent('You are here!')
                        .openOn(map);
            }
        </script>
    </body>
</html>
