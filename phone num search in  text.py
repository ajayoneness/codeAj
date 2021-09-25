from phonenumbers import PhoneNumberMatch

text="my phone num is +918603862290, and npali phone num is +9779844420651"
numbers= PhoneNumberMatch(text, "en")

for i in numbers:
    print(i)