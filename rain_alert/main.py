# api_key ='2f6e9279ff3633bc384c9d5f1ae9ef6f',69f04e4613056b159c2761a9d9e664d2
import requests
from twilio.rest import Client

account_sid = 'AC5428daa63215eaa5681322270c57fd77'
auth_token = '4dd0794297e0db1c1970f0578f78efb9'



Parameter = {
    'lat': 14.442599,
    'lon': 79.986458,
    'appid': "69f04e4613056b159c2761a9d9e664d2",
    'exclude': 'current,minutely,daily',

}
response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=Parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today ⛈⛈⛈.",
        from_='+18437556293',
        to='+918756967106'
    )
    print(message.status)

