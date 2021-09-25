import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder,carrier
phonenumber =phonenumbers.parse("+9779844420651","RO")
country=geocoder.description_for_number(phonenumber,"en")
timzon= timezone.time_zones_for_number(phonenumber)
c=carrier.name_for_number(phonenumber,"en")
v=phonenumbers.is_valid_number(phonenumber)
if v==True:
    print("\tWELCOME TO CODEAJ")
else:
    print("it is not valid num !! ")

print(f"company : {c}")
print(f"time zone : {timzon}")
print(f"countrty : {country}")