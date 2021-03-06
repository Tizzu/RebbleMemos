import json
import random
import string

import requests
from PyQt5.QtWidgets import QMessageBox

pinID = ""

# Get the token from file - if it's incorrect the server will return <Response[410>
f = open("token.txt", "r")
token = f.read().replace('\n', '')
f.close()


# Generate an unique ID for the pin
def randomString(stringLength=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# Populate the fields inside the JSON and send it to the server
def sendToTimeline(title, subtitle, body, time, icon, duration=-1):
    # Uncomment if feature is implemented - Pin editing
    #  if pinID == "":
    pinID = "RMPC-" + randomString()
    # Uncomment if feature is implemented - Pin editing
    # else : pinID = oldPin

    # Update the URL with the new ID
    url = "https://timeline-api.rebble.io/v1/user/pins/" + pinID
    # Header for the Timeline servers (it's not JSON)
    header = {'Content-Type': 'application/json',
              'X-User-Token': token}
    # This variable will become a JSON string, ready to be sent to the servers
    # the "time" field is built like this since it gives the local time with timezone 0 (instead of +01:00 or similar
    data = {}
    data["id"] = pinID
    data["time"] = str(time.date().year()) + "-" + leadingZero(time.date().month()) + "-" + leadingZero(
        time.date().day()) + "T" + leadingZero(time.time().hour()) + ":" + leadingZero(time.time().minute()) + ":00Z"
    layout = {}
    if duration != -1:
        data["duration"] = duration
        layout["type"] = "calendarPin"
    else:
        layout["type"] = "genericPin"
    layout["title"] = title
    layout["subtitle"] = subtitle
    layout["body"] = body
    layout["tinyIcon"] = "system://images/" + icon

    data["layout"] = layout
    response = requests.put(url, data=json.dumps(data), headers=header)
    if response.status_code == 200:
        alert = QMessageBox()
        alert.setWindowTitle('Rebble Memos')
        alert.setText('Memo sent successfully! \nIts ID is ' + pinID)
        alert.exec_()
    else:
        print(data)
        print(response)
        alert = QMessageBox()
        alert.setWindowTitle('Rebble Memos')
        reason = ""
        if response.status_code == 400:
            reason = "INVALID_JSON"
        elif response.status_code == 403:
            reason = "INVALID_API_KEY"
        elif response.status_code == 410:
            reason = "INVALID_USER_TOKEN"
        elif response.status_code == 429:
            reason = "RATE_LIMIT_EXCEEDED"
        elif response.status_code == 500:
            reason = "SERVICE_UNAVAILABLE"
        alert.setText('Something went wrong, Try again. \n Error: ' + reason)
        alert.exec_()


# Since I didn't find anything about adding a leading zero via library functions/parameters I've made a quick number
# to String converted where needed (Hours, Minutes, Days, Months)
def leadingZero(number):
    if 0 <= number <= 9:
        return "0" + str(number)
    else:
        return str(number)


# If you need to test your pin data without bothering the servers you can substitute sendToTimeline() inside memos.py with
# test(), so whe you click on the "Send to Timeline" button a dialog box will appear with the data submitted
# This function will also generate a JSON string in the terminal, so you can test the pin on an emulator
def test(title, subtitle, body, time, icon, duration=-1):
    data2 = {}
    data2["id"] = pinID
    data2["time"] = "" + str(time.date().year()) + "-" + leadingZero(time.date().month()) + "-" + leadingZero(
        time.date().day()) + "T" + leadingZero(time.time().hour()) + ":" + leadingZero(time.time().minute()) + ":00Z"
    layout = {}
    if duration != -1:
        data2["duration"] = duration
        layout["type"] = "calendarPin"
    else:
        layout["type"] = "genericPin"
    layout["title"] = title
    layout["subtitle"] = subtitle
    layout["body"] = body
    layout["tinyIcon"] = "system://images/" + icon

    data2["layout"] = layout
    print(json.dumps(data2))
    alert = QMessageBox()
    alert.setWindowTitle('Rebble Memos')
    alert.setText("Title: " + title + "\nSubtitle: " + subtitle + "\nBody: " + body + "\nTime/Date: " + str(
        time.date().year()) + "-" + leadingZero(time.date().month()) + "-" + leadingZero(
        time.date().day()) + "T" + leadingZero(time.time().hour()) + ":" + leadingZero(
        time.time().minute()) + ":00Z" + "\nIcon: " + icon + "\nDuration: " + str(duration))
    alert.exec_()
