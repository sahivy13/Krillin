from twilio.rest import Client

client = Client(
    "AC740ce6c7348d5301b0a7c7189a0dbd10", # ACCOUNT
    "cde6817141781b6c8557b60f3e83033a" # Token
)

for msg in client.messages.list():
    print(msg.body)