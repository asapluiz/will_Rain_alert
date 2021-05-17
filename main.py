import requests
from twilio.rest import Client

api_key = OPEN_WEATHER_API_KEY
account_sid = TWILIO_ACCT_ID
auth_token = TWILLIO_AUTH_TOKEN


params = {
    "lat": 53.079296,
    "lon": 8.801694,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

api = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params)
api.raise_for_status()
will_rain = False

for value in range(0, 13):
    if api.json()["hourly"][value]["weather"][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="its goint to rain today.",
        from_='+15017122661',
        to='+15558675310'
    )
    print(message.status)

