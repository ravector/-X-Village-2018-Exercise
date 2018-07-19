import requests

url ='https://www.metaweather.com/api/location/2306179/'

response = requests.get(url)
print(response.text)