import requests
from prettyprinter import pprint

response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=054&date=09-05-2021", auth = ('xyz', 'ert'))
pprint(response.json())