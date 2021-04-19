from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "e3d3c1974bb9c567f00c9b9ba1e17698"

@app.route('/')
def index():
    return 'App Works!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):

    url = 'https://samples.openweathermap.org/data/2.5/weather'
    params = dict(
        q=city + "," + country,
        appid= API_KEY,
    )

    response = requests.get(url=url, params=params)
    data = response.json()
    return data

@app.route('/test')
def test():
    return 'hello test'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
