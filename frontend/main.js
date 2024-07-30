document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([37.5665, 126.9780], 11);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    let marker;

    map.on('click', (e) => {
        const { lat, lng } = e.latlng;
        document.getElementById('lat').value = lat.toFixed(6);
        document.getElementById('lng').value = lng.toFixed(6);
        document.getElementById('buildDate').value = new Date().getFullYear() + '01'; // 例として現在年の1月を設定
    
        if (marker) {
            map.removeLayer(marker);
        }
        marker = L.marker([lat, lng]).addTo(map);
    });
    

    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // データが正しいか確認
        console.log('Form data:', data);

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'An unknown error occurred');
            }

            const result = await response.json();
            resultDiv.textContent = `予測価格は${result.predicted_price.toLocaleString()} KRWです。`;
            resultDiv.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            resultDiv.textContent = '予測処理中にエラーが発生しました。';
            resultDiv.style.display = 'block';
        }
    });

    // 初期状態で結果を非表示にする
    resultDiv.style.display = 'none';
});
