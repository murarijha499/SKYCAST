from flask import Flask, render_template, request
import requests

app = Flask(__name__)


api_key = '8e127bd81fa5486614eec3c28872d736'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        # API call to OpenWeatherMap
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return render_template('index.html', weather=weather)
        else:
            error_msg = "City not found!"
            return render_template('index.html', error=error_msg)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
