import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
API_key = os.getenv("API_key")

class Trailer:
    def __init__(self, MovieName: str = 'Barbie trailer'):
        self.TrailerData = {}
        self.fetch(MovieName)

    def getVidId(self):
        try:
                data = self.TrailerData["items"][0]["id"]["videoId"]
                return str(data)
        except (KeyError, IndexError):
            return None

    def fetch(self, MovieName):
            url = f"https://www.googleapis.com/youtube/v3/search" + \
            f"?key={API_key}&q={MovieName} trailer&aqi=no"
            response = requests.get(url)
            self.TrailerData = response.json()




# Create an instance of the Trailer class
'''moviet = Trailer("Finding nemo")

# Call the getVidId method
vid_id = moviet.getVidId()

print(vid_id)  # Print the video I'''