import googlemaps
import requests

def connection_gmap(key):
    '''
    Returns the interface to access the Google Maps API.

            Parameters:
                    key (str): Access token

            Returns:
                    Interface to access the Google Maps API
    '''
    return googlemaps.Client(key=key)

def address_to_coordinates(address, gmaps):
    '''
    Calculates coordinates based on an address.

            Parameters:
                    address (str): Address
                    gmaps: Interface to access the Google Maps API

            Returns:
                    (tuple): Pair of coordinates.
    '''
    geocode_result = gmaps.geocode(address)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']

    return (latitude, longitude)

def coordinates_to_neighborhood(latitude, longitude):
    '''
    Calculates the name of a neighborhood based on a pair of coordinates.

            Parameters:
                    latitude (float): Latitude
                    longitude (float): Longitude

            Returns:
                    (str): Name of a neighborhood
    '''
    url = 'https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query'
    parameters = {
        'where': '1=1',
        'geometry': f"{{'x':{longitude},'y':{latitude}}}",
        'f': 'json',
        'geometryType': 'esriGeometryPoint',
        'inSR': 4326,
    }
    
    response = requests.get(url, params=parameters)
    return response.json()['features'][0]['attributes']['NAME']

def add_value_address(address, value=100):
    '''
    Modifies the number of an address by adding an amount x to the value of the parameter.

            Parameters:
                    address (str): Address
                    value (float): Value

            Returns:
                    (str): Address with the modified number.
    '''
    address = address.split(" ")
    address[0] = int(address[0])
    address[0] += value
    address[0] = str(address[0])
    address = " ".join(address)
    
    return address

    
def neighboring_neighborhood(address, gmaps, neighboring):
    '''
    The name of the neighboring neighborhood is calculated.

            Parameters:
                    address (str): Address
                    gmaps: Interface to access the Google Maps API
                    neighboring (str): Name of the base neighborhood.

            Returns:
                    (str): Name of the neighboring neighborhood.
    '''
    latitude, longitude = address_to_coordinates(address, gmaps)
    neighborhood = coordinates_to_neighborhood(latitude, longitude)
    if( neighborhood != neighboring ):
        return neighborhood
    else:
        address = add_value_address(address)
        
        return neighboring_neighborhood(address, gmaps, neighboring)
