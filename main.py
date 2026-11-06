import requests
import os
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()



TWILIO_ACCOUNT_SID = os.getenv("TW_ACC")
TWILIO_AUTH_TOKEN = os.getenv("TW_TOK")

API_KEY = "27dabcd956a5bf6e8a9fd1a7422428b8"



LATITUDE=12.971599
LONGITUDE=77.594566
URL=f"https://api.openweathermap.org/data/2.5/forecast"
parameters={
    "lat":LATITUDE,
    "lon":LONGITUDE,
    "appid":API_KEY,
    "cnt":4

}
request=requests.get(URL,params=parameters)
request.raise_for_status()
data=request.json()
print(data)

weather_id=[data["list"][num]["weather"][0]["id"] for num in range(0,4)]

if any (id<700 for id in weather_id):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        to="+918527196801",
        from_="+17372508034",
        body="sms_appointment_reminders",
    )

    print(message.sid)

    print("Please bring your umbrella")
else:
    print("Enjoy it will not rain")

