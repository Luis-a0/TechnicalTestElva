import googlemaps
import requests

def connection_gmap(key):
    return googlemaps.Client(key=key)

def address_to_coordinates(address, gmaps):
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    return (lat, lng)

def coordinates_to_neighborhood(latitude, longitude):
    url = 'https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query'
    parameters = {
        'where': '1=1',
        'geometry': f"{'x':{longitude},'y':{latitude}}"
    }
    
    response = requests.get(url, params=parameters)
    print(response)

def neighboring_neighborhood(latitude, longitude, neighboring):
    neighborhood = coordinates_to_neighborhood(latitude, longitude)
    if(neighborhood != neighboring):
        return neighborhood
    else:
        return neighboring_neighborhood(latitude+100, longitude+100, neighboring)
