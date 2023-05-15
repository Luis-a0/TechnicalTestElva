from dotenv import load_dotenv
import os

from geoutilities import connection_gmap, address_coordinates
from geoutilities import coordinates_neighborhood, neighboring_neighborhood

load_dotenv()

if __name__ == "__main__":
    key = os.getenv('key')
    gmaps = connection_gmap(key)

    address = '1300 SE Stark Street, Portland, OR 97214'
    latitude, longitude = address_coordinates(address, gmaps)

    print(latitude, longitude)