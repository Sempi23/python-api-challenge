<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_efcd49668bebbb7d8219567ca2a65ebc {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
</head>
<body>
    
    
            <div class="folium-map" id="map_efcd49668bebbb7d8219567ca2a65ebc" ></div>
        
</body>
<script>
    
    
            var map_efcd49668bebbb7d8219567ca2a65ebc = L.map(
                "map_efcd49668bebbb7d8219567ca2a65ebc",
                {
                    center: [22.0752, -156.47],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_155a413c1563b24e2b26301f30677b2b = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );
        
    
            tile_layer_155a413c1563b24e2b26301f30677b2b.addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
            var marker_ff26d5c6aff18fcb4ceaf0c71fe6b9b4 = L.marker(
                [32.7026, -103.136],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_56f3300af0cbe049fe0f17dac7c56dbf = L.popup({"maxWidth": "100%"});

        
            
                var html_5c5da8e52d47f54499eb0d1531c44028 = $(`<div id="html_5c5da8e52d47f54499eb0d1531c44028" style="width: 100.0%; height: 100.0%;">hobbs, US - None</div>`)[0];
                popup_56f3300af0cbe049fe0f17dac7c56dbf.setContent(html_5c5da8e52d47f54499eb0d1531c44028);
            
        

        marker_ff26d5c6aff18fcb4ceaf0c71fe6b9b4.bindPopup(popup_56f3300af0cbe049fe0f17dac7c56dbf)
        ;

        
    
    
            var marker_adbea23f15a9ec459e07d4d1eb869b69 = L.marker(
                [37.0373, -95.6164],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_947c73aaa9396243954c727b61dc163d = L.popup({"maxWidth": "100%"});

        
            
                var html_12dc7ced54acad022355f5791b060a57 = $(`<div id="html_12dc7ced54acad022355f5791b060a57" style="width: 100.0%; height: 100.0%;">coffeyville, US - None</div>`)[0];
                popup_947c73aaa9396243954c727b61dc163d.setContent(html_12dc7ced54acad022355f5791b060a57);
            
        

        marker_adbea23f15a9ec459e07d4d1eb869b69.bindPopup(popup_947c73aaa9396243954c727b61dc163d)
        ;

        
    
    
            var marker_478b9f08a37c08d8a81de6185a889897 = L.marker(
                [19.6406, -155.9956],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_dd966f9155e25111fb84ba52922d115a = L.popup({"maxWidth": "100%"});

        
            
                var html_8a06e3ea58e353de84711960f8173daf = $(`<div id="html_8a06e3ea58e353de84711960f8173daf" style="width: 100.0%; height: 100.0%;">kailua-kona, US - None</div>`)[0];
                popup_dd966f9155e25111fb84ba52922d115a.setContent(html_8a06e3ea58e353de84711960f8173daf);
            
        

        marker_478b9f08a37c08d8a81de6185a889897.bindPopup(popup_dd966f9155e25111fb84ba52922d115a)
        ;

        
    
    
            var marker_67fc5f231c1794fc5f76c7c76f59524e = L.marker(
                [19.6228, -155.9522],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_a28242cc3ffa860df01670f88a1254e8 = L.popup({"maxWidth": "100%"});

        
            
                var html_e23755d6122f4c68a42b71c9e3ab194f = $(`<div id="html_e23755d6122f4c68a42b71c9e3ab194f" style="width: 100.0%; height: 100.0%;">holualoa, US - None</div>`)[0];
                popup_a28242cc3ffa860df01670f88a1254e8.setContent(html_e23755d6122f4c68a42b71c9e3ab194f);
            
        

        marker_67fc5f231c1794fc5f76c7c76f59524e.bindPopup(popup_a28242cc3ffa860df01670f88a1254e8)
        ;

        
    
    
            var marker_15d1399417078279a26e8dd980a3893e = L.marker(
                [28.629, -17.9293],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_55b8b7bcaf2322d099136b86e32e82ca = L.popup({"maxWidth": "100%"});

        
            
                var html_67b81f4465a2f7b925a3c342314ea969 = $(`<div id="html_67b81f4465a2f7b925a3c342314ea969" style="width: 100.0%; height: 100.0%;">tazacorte, ES - None</div>`)[0];
                popup_55b8b7bcaf2322d099136b86e32e82ca.setContent(html_67b81f4465a2f7b925a3c342314ea969);
            
        

        marker_15d1399417078279a26e8dd980a3893e.bindPopup(popup_55b8b7bcaf2322d099136b86e32e82ca)
        ;

        
    
    
            var marker_5458a272e5fe93ee9698e67b08ce6f43 = L.marker(
                [29.0605, -13.564],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_1cf14022240539419cf75b5c530234be = L.popup({"maxWidth": "100%"});

        
            
                var html_683e4986bad2f19d092cf941bf570b03 = $(`<div id="html_683e4986bad2f19d092cf941bf570b03" style="width: 100.0%; height: 100.0%;">teguise, ES - None</div>`)[0];
                popup_1cf14022240539419cf75b5c530234be.setContent(html_683e4986bad2f19d092cf941bf570b03);
            
        

        marker_5458a272e5fe93ee9698e67b08ce6f43.bindPopup(popup_1cf14022240539419cf75b5c530234be)
        ;

        
    
    
            var marker_6139fd615d302db3a1c7370f077592a8 = L.marker(
                [33.0393, -85.0313],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_aac1f40d529525df8f200da3fe80dc70 = L.popup({"maxWidth": "100%"});

        
            
                var html_841e72567395f55990567c51f950c4a5 = $(`<div id="html_841e72567395f55990567c51f950c4a5" style="width: 100.0%; height: 100.0%;">lagrange, US - None</div>`)[0];
                popup_aac1f40d529525df8f200da3fe80dc70.setContent(html_841e72567395f55990567c51f950c4a5);
            
        

        marker_6139fd615d302db3a1c7370f077592a8.bindPopup(popup_aac1f40d529525df8f200da3fe80dc70)
        ;

        
    
    
            var marker_cae2032946838429dcc12597070bc492 = L.marker(
                [-33.918, 25.5701],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_c1f6510192bdbf749fd3646d3c22bcfb = L.popup({"maxWidth": "100%"});

        
            
                var html_0b8f5ac31d6cfc9ca1aae9f51e81dd8d = $(`<div id="html_0b8f5ac31d6cfc9ca1aae9f51e81dd8d" style="width: 100.0%; height: 100.0%;">port elizabeth, ZA - None</div>`)[0];
                popup_c1f6510192bdbf749fd3646d3c22bcfb.setContent(html_0b8f5ac31d6cfc9ca1aae9f51e81dd8d);
            
        

        marker_cae2032946838429dcc12597070bc492.bindPopup(popup_c1f6510192bdbf749fd3646d3c22bcfb)
        ;

        
    
    
            var marker_313bccb768fbad343e04491bb6a116c7 = L.marker(
                [45.0141, 8.6414],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_be3d24b723f7e259a7941a6c6951b4a0 = L.popup({"maxWidth": "100%"});

        
            
                var html_494fa9549f4943dfad2a3f8af205a4d9 = $(`<div id="html_494fa9549f4943dfad2a3f8af205a4d9" style="width: 100.0%; height: 100.0%;">valenza, IT - None</div>`)[0];
                popup_be3d24b723f7e259a7941a6c6951b4a0.setContent(html_494fa9549f4943dfad2a3f8af205a4d9);
            
        

        marker_313bccb768fbad343e04491bb6a116c7.bindPopup(popup_be3d24b723f7e259a7941a6c6951b4a0)
        ;

        
    
    
            var marker_a2e73d66841b33a72cd67d119558e250 = L.marker(
                [46.9531, 54.0198],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_172463a3b8ce3c80e39268ea90889cc9 = L.popup({"maxWidth": "100%"});

        
            
                var html_9dae4c1e4bb2a9239665dbeae16248c2 = $(`<div id="html_9dae4c1e4bb2a9239665dbeae16248c2" style="width: 100.0%; height: 100.0%;">qulsary, KZ - None</div>`)[0];
                popup_172463a3b8ce3c80e39268ea90889cc9.setContent(html_9dae4c1e4bb2a9239665dbeae16248c2);
            
        

        marker_a2e73d66841b33a72cd67d119558e250.bindPopup(popup_172463a3b8ce3c80e39268ea90889cc9)
        ;

        
    
    
            var marker_45a0f0827e1359a2c36a8939c4260c2b = L.marker(
                [25.2088, 64.6357],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_9fef75761c7af09b461ff61a5cdbe441 = L.popup({"maxWidth": "100%"});

        
            
                var html_8d412a040a52b6b42b8d3dda3c5fec26 = $(`<div id="html_8d412a040a52b6b42b8d3dda3c5fec26" style="width: 100.0%; height: 100.0%;">ormara, PK - None</div>`)[0];
                popup_9fef75761c7af09b461ff61a5cdbe441.setContent(html_8d412a040a52b6b42b8d3dda3c5fec26);
            
        

        marker_45a0f0827e1359a2c36a8939c4260c2b.bindPopup(popup_9fef75761c7af09b461ff61a5cdbe441)
        ;

        
    
    
            var marker_06cd7e38170f638d4ec7ba810d9b5435 = L.marker(
                [36.7025, 52.6576],
                {}
            ).addTo(map_efcd49668bebbb7d8219567ca2a65ebc);
        
    
        var popup_d489a651c4fcf3de361571ea3b91014d = L.popup({"maxWidth": "100%"});

        
            
                var html_7183a1ca20ff3a983c3a79fb8ddd9968 = $(`<div id="html_7183a1ca20ff3a983c3a79fb8ddd9968" style="width: 100.0%; height: 100.0%;">babolsar, IR - None</div>`)[0];
                popup_d489a651c4fcf3de361571ea3b91014d.setContent(html_7183a1ca20ff3a983c3a79fb8ddd9968);
            
        

        marker_06cd7e38170f638d4ec7ba810d9b5435.bindPopup(popup_d489a651c4fcf3de361571ea3b91014d)
        ;

        
    
</script>
</html>