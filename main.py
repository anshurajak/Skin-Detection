# import phonenumbers
# import opencage
# import folium
# from test import number

# from phonenumbers import geocoder

# pepnumber = phonenumbers.parse(number)

# location = phonenumbers.parse(number,'en')
# print(geocoder.description_for_number(location,"en"))

# from phonenumbers import carrier
# service_name = phonenumbers.parse(number,"RO")
# print(carrier.name_for_number(service_name,"en"))

# from opencage.geocoder import OpenCageGeocode

# key = "0d06a4dfd9814390a0115bb7a65dabe3"

# geocoder = OpenCageGeocode(key)
# query = str(location)

# results = geocoder.geocode(query)
# print(results)

# lat = results[0]['geocoder']['lat']
# lng = results[0]['geocoder']['lng']

# print(lat,lng)

# myMap = folium,Map(location=[lat,lng], zoom_start =_9)
# folium.Marker([lat,lng], popup= location).add_to(myMap)

# myMap.save("mylocation.html")



# import phonenumbers
# from phonenumbers import geocoder, carrier

# # Enter phone number along with country code
# number = input("Enter phone number with country code: ")

# # Parsing String to the Phone number
# phoneNumber = phonenumbers.parse(number)

# # printing the timezone using the timezone module
# timeZone = phonenumbers.time_zones_for_number(phoneNumber)
# print("Timezone: " + str(timeZone))

# # printing the geolocation of the given number using the geocoder module
# geolocation = geocoder.description_for_number(phoneNumber, "en")
# print("Location: " + geolocation)

# # printing the service provider name using the carrier module
# service = carrier.name_for_number(phoneNumber, "en")
# print("Service Provider: " + service)


# import os
# from twilio.rest import Client

# # Your Account SID from twilio.com/console
# account_sid = "your_account_sid"
# # Your Auth Token from twilio.com/console
# auth_token  = "your_auth_token"
# client = Client(account_sid, auth_token)

# # Enter phone number along with country code
# number = input("Enter phone number with country code: ")

# lookup_response = client.lookups \
#                          .phone_numbers(number) \
#                          .fetch(type="caller-name")

# print(lookup_response.caller_name)




import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Enter phone number along with country code
number = input("Enter phone number with country code: ")

# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

# Get geolocation of the phone number
geolocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + geolocation)

# Get service provider name
service = carrier.name_for_number(phoneNumber, "en")
print("Service Provider: " + service)

# OpenCage API key
key = "your_opencage_api_key"  # Replace with your OpenCage API key
geocoder_api = OpenCageGeocode(key)

# Fetch latitude and longitude using OpenCage API
query = str(geolocation)
results = geocoder_api.geocode(query)

if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map using folium
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=geolocation).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("mylocation.html")
    print("Map has been saved as 'mylocation.html'. Open it in a browser to view the location.")
else:
    print("Could not fetch location coordinates.")