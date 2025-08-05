function initMap() {
            const ruta = { lat: 2.444814, lng: -76.614739 };
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: ruta,
            });
            new google.maps.Marker({
                position: ruta,
                map: map,
                title: "Inicio de la Ruta Torre 24",
            });
        }
        
        /* vista 2 ks */


    
        const map = L.map('map').setView([2.441, -76.606], 13); 

     
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        
        L.marker([2.441, -76.606]).addTo(map)
            .bindPopup('<b>El Morro</b><br>Inicio de la ruta de senderismo.')
            .openPopup();