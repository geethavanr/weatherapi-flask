from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_info = None
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']
        
        api_key = '6bee6d8f025bd470f9e0d7ccb00004f2'  #API Key from openweathermap
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
        
        #Print the URL
        print(url)
        print("Fingers Crossed!!")
        
        response = requests.get(url)
        
        # Print the response JSON for debugging
        print(response.json())
        
        if response.status_code == 200:
            data = response.json()
            if 'main' in data and 'weather' in data:
                weather_info = {
                    'temperature': data['main'].get('temp', 'N/A'),
                    'description': data['weather'][0].get('description', 'N/A'),
                    'city': data.get('name', 'Unknown'),
                    'country': data['sys'].get('country', 'Unknown')
                }
            else:
                weather_info = {'error': 'Weather data not available!'}
        else:
            weather_info = {'error': 'City not found!'}

    return render_template('index.html', weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
