from twilio.rest import Client
from django.conf import settings

# account_sid = 'ACa9b3a79bcacc0ec38c29135fc5e395d1'
# auth_token = '85aa55fb1024bfe53a8d05104af76b91'
# TWILIO_ACCOUNT_SID = 'ACf9539e42d9b32b5c9b190237d6a3ae35'
# TWILIO_AUTH_TOKEN = '6e78b5793d80aaeb1af3c0206057e648'
account_sid = 'ACf9539e42d9b32b5c9b190237d6a3ae35'
auth_token = '6e78b5793d80aaeb1af3c0206057e648'
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def verifications(phone_number, via):
        return client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verifications.create(to=phone_number, channel=via)

def verification_checks(phone_number, token):
        return client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verification_checks.create(to=phone_number, code=token)