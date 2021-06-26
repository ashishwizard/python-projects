import phonenumbers
from phonenumbers import geocoder,carrier
import folium
key='a84da425daf54038bf902653bb6dcbf5'

phoneNUM=phonenumbers.parse("+917735661439") #write your desired phone no. in place of xxxx

carrier=carrier.name_for_number(phoneNUM,'en')

Region=geocoder.description_for_number(phoneNUM,'en')

print(carrier)
print(Region)
from opencage.geocoder import OpenCageGeocode
geocoder= OpenCageGeocode(key)
query = str(Region)

results=geocoder.geocode(query)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=Region).add_to((myMap))

myMap.save("mylocation.html")


