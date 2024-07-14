$(document).ready(function() {
    var surveyJSON = {
        pages: [
            {
                questions: [
                    {
                        type: "html",
                        name: "mappa",
                        html: "<div id='map'></div>"
                    }
                ]
            }
        ]
    };

    function initMap() {
        var map = L.map('map').setView([40.7128, -74.0060], 13); // Usa le coordinate iniziali desiderate
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        var marker;

        map.on('click', function(e) {
            if (marker) {
                map.removeLayer(marker);
            }
            marker = L.marker(e.latlng).addTo(map);
            // Qui puoi aggiungere logica per salvare le coordinate del marker o per aggiornare il survey
            console.log(e.latlng); // Stampa le coordinate nel console
        });
    }

    function onSurveyRendered() {
        initMap();
    }

    var survey = new Survey.Model(surveyJSON);
    $("#surveyContainer").Survey({
        model: survey,
        onComplete: function(result) {
            console.log(result.data);
            // Qui puoi gestire i dati del form alla loro submission
        },
        onAfterRenderSurvey: onSurveyRendered
    });
});

function waitForElementToDisplay(selector, time) {
    if(document.querySelector(selector) != null) {
        initMap();
    } else {
        setTimeout(function() {
            waitForElementToDisplay(selector, time);
        }, time);
    }
}

function onSurveyRendered() {
    waitForElementToDisplay("#map", 500); // Controlla ogni 500ms
}