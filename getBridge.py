#! python3
# getBridge.py - Prints the status of the bridges.
# Created by Nelson Hickman

import json
import requests

# Download the JSON data from mulnomah county's API.
url ='https://api.multco.us/bridges?access_token=YOUR-TOKEN-HERE
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
bridge_data = json.loads(response.text)

#Loop through the bridges and print status

for i in bridge_data:
    if not i['isUp']:
        print(i['name'] + ' is down')
    elif i['isUp']:
        print(i['name'] + ' is up')

# List of bridges that TriMet cares about
bridge_list = ['hawthorne', 'morrison', 'burnside', 'broadway']

# function to get next scheduled lift
def get_bridge_schedule(bridge):
    scheduleUrl = 'https://api.multco.us/bridges/%s/events/scheduled?access_token=YOUR-TOKEN-HERE' %(bridge)
    schedule_response = requests.get(scheduleUrl)
    schedule_response.raise_for_status()

    schedule_bridge_data = json.loads(schedule_response.text)
    if schedule_bridge_data != []:
        print('The next scheduled lift for %s is: ' + schedule_bridge_data[0] %(bridge))
    else:
        print('no secheduled lift for %s' %(bridge))

# get next scheduled lift
for i in bridge_list:
    get_bridge_schedule(i)