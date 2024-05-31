# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# service = client.messaging \
#                 .v1 \
#                 .services \
#                 .create(friendly_name='My First Messaging Service')

# print(service.sid)


account_sid = "ACe2920d32a51a1a287e57a7c2ec0d0cdb"
auth_token  = "e57009095c411bb848f2622812dd78d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918791410352",
    from_="+17064034247",
    body="Hello from Python!")

print(message.sid)