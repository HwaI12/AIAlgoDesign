new Vue({
    el: '#app',
    data: {
        map: null,
        properties: [],
        predictionInput: {
            m2: 0,
            p: 0,
            buildDate: 0
        },
        predictionResult: null
    },
    mounted() {
        this.initMap();
        this.fetchData();
    },
    methods: {
        initMap() {
            this.map = L.map('map').setView([37.5665, 126.9780], 11);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
        },
        fetchData() {
            fetch('http://localhost:5000/data')
                .then(response => response.json())
                .then(data => {
                    this.properties = data;
                    this.plotProperties();
                });
        },
        plotProperties() {
            this.properties.forEach(property => {
                L.marker([property.lat, property.lng]).addTo(this.map)
                    .bindPopup(`面積: ${property.m2}m², 階数: ${property.p}`);
            });
        },
        predict() {
            fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.predictionInput),
            })
                .then(response => response.json())
                .then(data => {
                    this.predictionResult = data.predicted_price;
                });
        }
    }
});