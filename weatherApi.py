from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 
url = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            weather_desc = data['weather'][0]['description']
            weather = {'temp': temp, 'humidity': humidity, 'wind_speed': wind_speed, 'weather_desc': weather_desc}
        else:
            weather = None
        return render_template('index.html', city=city, weather=weather)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
