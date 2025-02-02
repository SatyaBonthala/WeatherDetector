import requests

# Function to get weather data
def get_weather(city):
    # Your OpenWeatherMap API key
    api_key = '997ce4aa5335e0d647e5324c7447e3d1'
    
    # URL for the weather API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    # Sending a GET request to the API
    response = requests.get(url)
    
    # If the response status code is 200 (success)
    if response.status_code == 200:
        data = response.json()
        
        # Extracting useful data from the response
        city_name = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        
        # Printing the weather data
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print("City not found or invalid API key.")

# Ask the user for a city name
city = input("Enter city name: ")

# Call the function to get weather
get_weather(city)
