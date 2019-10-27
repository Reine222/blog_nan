from twilio.rest import Client

# account_sid = 'AC87bcdc10483708c4d174405099e1bedd'
#             auth_token =  '5b0fd2340344516a0f43bf8ca5deb864'
#             client = Client(account_sid, auth_token)

#             message = client.messages \
#                             .create(
#                                 body="Votre Code de validation est le suivant:",
#                                 from_= '+12057053851',
#                                 to= '+22553858586',
#                             )
#                             print(message.sid)
                            
                            
account_sid = 'AC87bcdc10483708c4d174405099e1bedd'
auth_token = '5b0fd2340344516a0f43bf8ca5deb864'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='Votre Code de validation est le suivant:',
        from_='+12057053851',
        to='+22589485436'
    )

print(message.sid)