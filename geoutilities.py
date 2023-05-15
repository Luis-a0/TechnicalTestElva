import googlemaps

def connection_gmap(key):
    return googlemaps.Client(key=key)

def address_coordinates(address, gmaps):
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    return (lat, lng)

def coordinates_neighborhood(lat, lng):
    pass

def neighboring_neighborhood(neighboring, neighborhood='', move=100):
    pass