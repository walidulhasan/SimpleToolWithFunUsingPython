from twilio.rest import Client

SID='AC7a572fd3d91f8e0dad895a0c82fa5bce'
Auth_Token='512951a2fbf6ad5c140989016e81f4ddd'

cl=Client(SID,Auth_Token)

cl.messages.create(body=input("Your Message Please: "),from_='+12284521596',to=input("To User Number With Country: "))
print('Successfully Send Your Message !!')
                   
