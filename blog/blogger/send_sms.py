from twilio.rest import Client

# account_sid = 'AC87bcdc10483708c4d174405099e1bedd'
#             auth_token =  '5b0fd2340344516a0f43bf8ca5deb864'
#             client = Client(account_sid, auth_token)

#             message = client.messages \
#                             .create(
#                                 body="Votre Code de validation est le suivant:",
#                                 from_= '+12057053851',
# #                                 to= '+22553858586',
# #                             )
# #                             print(message.sid)
                            
                            
# account_sid = 'AC87bcdc10483708c4d174405099e1bedd'
# auth_token = '5b0fd2340344516a0f43bf8ca5deb864'
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#         body='Votre Code de validation est le suivant:',
#         from_='+12057053851',
#         to='+22589485436'
#     )

# print(message.sid)




# def genere():
#     code='BlogNan2019*'
#     account_sid = 'ACcd70283e1ee00056836d33ddb10ceb53'
#     auth_token = 'b3169a7d3ed1082856a8dd7c5f9f3432'
#     client = Client(account_sid, auth_token)

#     message = client.messages \
#         .create(
#             body='Votre Code de validation est le suivant: {}'.format(code),
#             from_='+18049772449',
#             to='+22553858586'
#         )
#     return(message.sid)