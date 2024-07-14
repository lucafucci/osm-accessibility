let map;
let marker;


document.addEventListener('DOMContentLoaded', function() {
    // Inizializza la mappa
    map = L.map('map').setView([40.712776, -74.005974], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Aggiungi il controllo di geolocalizzazione
    L.control.locate({
        position: 'topright', // Posizione del pulsante sulla mappa
        drawCircle: false, // Disegna un cerchio intorno alla posizione dell'utente
        follow: false, // Segue la posizione dell'utente mentre si muove
        setView: 'always', // Centra automaticamente la mappa sulla posizione dell'utente
        watch: false, // Aggiorna la posizione dell'utente mentre si muove
        keepCurrentZoomLevel: false, // Permette di cambiare il livello di zoom quando localizza
        flyto: true, // Effetto di volo quando localizza
        markerStyle: {
            weight: 1,
            opacity: 0.8,
            fillOpacity: 0.8
        },
        circleStyle: {
            weight: 1,
            clickable: false
        },
        icon: 'fa fa-crosshairs', // Usa un'icona FontAwesome per il pulsante
        metric: true,
        strings: {
            title: "Mostra dove mi trovo", // Testo mostrato al passaggio del mouse sul pulsante
        },
        locateOptions: {
            maxZoom: 10,
            watch: true,
            enableHighAccuracy: true,
        }
    }).addTo(map);
});



