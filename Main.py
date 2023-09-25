import schedule
def get_weather(latitude, longitude):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_text_message(body):
    account_sid = 'twilio_sid'
    auth_token = 'twilio_token'
    from_phone_number = 'twilio_phone_number'
    to_phone_number = 'my_number'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print('Message sent!')
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32
def send_weather_update():
    latitude = 34.633980
    longitude = -86.734910

    weather_data = get_weather(latitude, longitude)
    tempurature = weather_data['hourly']['temperature_2m']
    relative_humidity = weather_data['hourly']['relativehumidity_2m']
    wind_speed = weather_data['hourly']['windspeed_10m'][0]
    tempurature_farenhiet = celcius_to_fahrenheit(tempurature)

    weather_info = {
        'Good Morning! \n'
        'Current weather: \n'
        f'Temperature: {tempurature_farenhiet} \n'
        f'Relative Humidity: {relative_humidity} \n'
        f'Wind Speed: {wind_speed} m/s'

    }
    send_text_message(weather_info)
    
def main():
    schedule.every().day.at("8:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
