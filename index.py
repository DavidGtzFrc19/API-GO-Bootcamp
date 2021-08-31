# Import the framework Flask
from flask import Flask, render_template, request
import requests
from requests.api import post

# Create an instance of Flask
app = Flask(__name__)

# First EndPoint
@app.route('/hello')
def hello():
    name = "Hello, world!"
    return name

# Second EndPoint
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['post'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=a21e96fc78843a8e2fb7b444b8e08aa9')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = (temp_k - 273.15)
    return render_template('temperature.html', temp=temp_c)


if __name__ == "__main__":
    app.run(debug=True)