#! python3
# getBridge.py - Prints the status of the bridges.
# Created by Nelson Hickman

import json, requests

# Download the JSON data from mulnomah county's API.
url ='https://api.multco.us/bridges?access_token=YOUR-TOKEN-HERE'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
bridgeData = json.loads(response.text)

#Loop through the bridges and print status

for i in bridgeData:
    if i['isUp'] == False:
        print(i['name'] + ' is down')
    elif i['isUp'] == True:
        print(i['name'] + ' is up')

# List of bridges that X cares about
bridgeList = ['hawthorne', 'morrison', 'burnside', 'broadway']

# function to get next scheduled lift
def getBridgeSchedule(bridge):
    scheduleUrl = 'https://api.multco.us/bridges/%s/events/scheduled?access_token=YOUR-TOKEN-HERE' %(bridge)
    scheduleResponse = requests.get(scheduleUrl)
    scheduleResponse.raise_for_status()

    scheduleBridgeData = json.loads(scheduleResponse.text)
    if scheduleBridgeData != []:
        print(f'The next scheduled lift for {bridge} is: ' + scheduleBridgeData[0])
    else:
        print('no secheduled lift for %s' %(bridge))

# get next scheduled lift
for i in bridgeList:
    getBridgeSchedule(i)