from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = ''  # Replace with your API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return jsonify(weather)
    else:
        return jsonify({'error': 'Could not retrieve weather data'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
