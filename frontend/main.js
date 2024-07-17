new Vue({
    el: '#app',
    data: {
        map: null,
        properties: [],
        predictionInput: {
            m2: 0,
            p: 0,
            buildDate: 2000
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
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    this.properties = data;
                    this.plotProperties();
                    this.createScatterPlot();
                });
        },
        plotProperties() {
            this.properties.forEach(property => {
                L.marker([property.lat, property.lng]).addTo(this.map)
                    .bindPopup(`面積: ${property.m2}m², 階数: ${property.p}, スコア: ${property.score}`);
            });
        },
        predict() {
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.predictionInput),
            })
                .then(response => response.json())
                .then(data => {
                    this.predictionResult = data.predicted_score;
                });
        },
        createScatterPlot() {
            const trace = {
                x: this.properties.map(p => p.m2),
                y: this.properties.map(p => p.score),
                mode: 'markers',
                type: 'scatter',
                marker: { size: 5 }
            };
            const layout = {
                title: '面積とスコアの関係',
                xaxis: { title: '面積 (m²)' },
                yaxis: { title: 'スコア' }
            };
            Plotly.newPlot('scatter-plot', [trace], layout);
        }
    }
});