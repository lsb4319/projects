import requests
import json
import webbrowser
from selenium import webdriver


url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    url = "https://www.google.com/maps/search/?api=1&query={0}%2c{1}".format(latitude,longitude)
    driver = webdriver.Chrome()
    driver.get(url)
    webbrowser.open(url)
else: 
    print("Error fetching ISS location data.")