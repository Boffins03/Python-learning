# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACe2920d32a51a1a287e57a7c2ec0d0cdb"
auth_token  = "e57009095c411bb848f2622812dd78d0"
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=20)

for record in messages:
    data = json.load(record)
    print(record.sid)

print(data)