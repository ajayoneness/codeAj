import random
from twilio.rest import Client

randomotp=random.randint(100000,999999)

firstname= input("first name : ")
lastname=input ("last name : ")
phoneno=input ("phone no. : +91 ")
print ("otp is sent in your given mobile number  ")

#API code part 
account_sid = 'AC60f1aa727b2baf6d32c18fce64a6d215'
auth_token = '7fabcd603876b393157e646b5d134882'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body=f"OTP for verification process is {randomotp}\nsent by codeaj",
                     from_='+19855098726',
                     to=f'+91{phoneno}')

otp =input ("enter OTP : ")
if str(randomotp) == otp:
    print ("your account is verified by codeaj ")
else :
    print("entered otp is incorrect !! ")

print(message.sid)

with open (f'{firstname}','w')as f:
    f.write(message.sid)

