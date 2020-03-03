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
def sendToTimeline(title, subtitle, body, time, icon):
    # Uncomment if feature is implemented - Pin editing
    #  if pinID == "":
    pinID = randomString()
    # Uncomment if feature is implemented - Pin editing
    # else : pinID = oldPin

    # Update the URL with the new ID
    url = "https://timeline-api.rebble.io/v1/user/pins/" + pinID
    # Header for the Timeline servers (it's not JSON)
    header = {'Content-Type': 'application/json',
              'X-User-Token': token}
    #This variable will become a JSON string, ready to be sent to the servers
    # the "time" field is built like this since it gives the local time with timezone 0 (instead of +01:00 or similar
    data = {
        "id": pinID,
        "time": "" + str(time.date().year()) + "-" + str(time.date().month()) + "-" + str(
            time.date().day()) + "T" + str(time.time().hour()) + ":" + str(time.time().minute()) + ":00Z",
        "layout": {
            "type": "genericPin",
            "title": title,
            "subtitle": subtitle,
            "body": body,
            "tinyIcon": "system://images/" + icon
        }
    }
    response = requests.put(url, data=json.dumps(data), headers=header)
    if response.status_code == 200:
        alert = QMessageBox()
        alert.setWindowTitle('Rebble Memos')
        alert.setText('Memo sent successfully! \nIts ID is ' + pinID)
        alert.exec_()
    else:
        alert = QMessageBox()
        alert.setWindowTitle('Rebble Memos')
        alert.setText('Something went wrong, Try again. \n Error code:' + str(response.status_code))
        alert.exec_()


# If you need to test your pin data without bothering the servers you can substitute sendToTimeline() inside memos.py with
# test(), so whe you click on the "Send to Timeline" button a dialog box will appear with the data submitted
# This function will also generate a JSON string in the terminal, so you can test the pin on an emulator
def test(title, subtitle, body, time, icon):
    data2 = {
        "id": "pinID",
        "time": "" + str(time.date().year()) + "-" + str(time.date().month()) + "-" + str(
            time.date().day()) + "T" + str(time.time().hour()) + ":" + str(time.time().minute()) + ":00Z",
        "layout": {
            "type": "genericPin",
            "title": title,
            "subtitle": subtitle,
            "body": body,
            "tinyIcon": "system://images/" + icon
        }
    }
    print(json.dumps(data2))
    alert = QMessageBox()
    alert.setWindowTitle('Rebble Memos')
    alert.setText("Title: " + title + "\nSubtitle: " + subtitle + "\nBody: " + body + "\nTime/Date: " + str(
        time.date().year()) + "-" + str(time.date().month()) + "-" + str(time.date().day()) + "T" + str(
        time.time().hour()) + ":" + str(time.time().minute()) + ":00Z" + "\nIcon: " + icon)
    alert.exec_()
