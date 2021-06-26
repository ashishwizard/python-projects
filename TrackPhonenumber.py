from opencage.geocoder import OpenCageGeocode
import phonenumbers
from phonenumbers import geocoder, carrier
import folium
key = 'xxxxxxxxxxxxx'

# write your desired phone no. in place of xxxx
phoneNUM = phonenumbers.parse("+91xxxxxx")

carrier = carrier.name_for_number(phoneNUM, 'en')

Region = geocoder.description_for_number(phoneNUM, 'en')

print(carrier)
print(Region)
# goto opencage.com and create a account free to get a api key and paste it in key ='xxx'.
geocoder = OpenCageGeocode(key)
query = str(Region)

results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=Region).add_to((myMap))

# saves a html file with geolocation of phone number
myMap.save("mylocation.html")
