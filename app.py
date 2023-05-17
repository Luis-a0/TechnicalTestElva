from dotenv import load_dotenv
import os

from geoutilities import connection_gmap, address_to_coordinates
from geoutilities import coordinates_to_neighborhood, neighboring_neighborhood

load_dotenv()

if __name__ == "__main__":
    key = os.getenv('key')
    gmaps = connection_gmap(key)

    address = '1300 SE Stark Street, Portland, OR 97214'
    latitude, longitude = address_to_coordinates(address, gmaps)

    neighborhood_base = coordinates_to_neighborhood(latitude, longitude)

    neighborhood_2 = neighboring_neighborhood(address, gmaps, neighborhood_base)
    print(f"The neighborhood with the X={longitude} Y={latitude} coordinates is \
{neighborhood_base} and the neighborhood next to it is {neighborhood_2}.")