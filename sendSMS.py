from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC64bff1796402535465c9bebe442d1f18"
auth_token = "73e624975dec2ef220940fea6467ce9e"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                     body="Hello there!")
                                     
