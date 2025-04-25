import requests

# Get your free API key from OpenWeatherMap
api_key = 'YOUR_API_KEY'

# Enter the city you want to get weather for
city = 'London'

# Create the API URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Send the request to the API
response = requests.get(url)

# Convert the response to JSON
data = response.json()

# Get the current temperature
temperature = data['main']['temp']

# Print the temperature
print(f"The current temperature in {city} is {temperature}°C.")
