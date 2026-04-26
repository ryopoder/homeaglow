import os
# from twilio.rest import Client
# from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

class Client:

    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token


class TwilioClient:

    def __init__(self):
        account_sid = "sid" #os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = "token" #os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

    def send_text(self, from_phone, to_phone, message):
        self.client.messages.create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            # TODO I think this comes from the Room b/c that will be the twilio number and not from the user
            from_="+15017122661",
            to="+15558675310",
        )
        print(f'sent message {message} to {to_phone} from {from_phone}')
        return True
