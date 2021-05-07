import requests, play_song, string, random, time
from prettyprinter import pprint

def generate_random():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))
    return ran

check = False

username = "pborthak"
password = "pw1234"

while(True):
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=054&date=09-05-2021", 
    auth = (username, password))
    
    if check:
        break

    if response.status_code == 200:
        response = response.json()
        pprint(response)

        if len(response['sessions']) != 0:
            check = True
            pprint(response)

    else:
        print(response.status_code)
        print("Sleeping now...")
        time.sleep(100)
        username = generate_random()
        print("Up and Running again!\n")

    time.sleep(5)

if check:
    play_song.play('Levitating.mp3')