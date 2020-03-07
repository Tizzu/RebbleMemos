# Rebble Memos
This Application lets you push custom memos to a Rebble-enabled Pebble smartwatch

The application lets you define a title for your memo, a subtitle (visible from the timeline) and a body (visible within the pin itself). You can also define a time and date, and also select the Memo icon from a selection of built-in Pebble icons.
***
### Build and compile
This project makes use of the "requests" and "PyQt5" modules, you can install them by issuing
```
pip install requests PyQt5
		or
pip install - r requirements.txt

```

To get a working executable you can use the following command in a terminal:
```
pyinstaller -F --noconsole --clean memos.spec
```
You can run the code without creating an .exe file, but unfortunately it won't show up any images (because the code is designed to look up for relative paths inside the executable) so unless you need the debugging features of your IDE it's recommended to use pyinstaller and test the program as a standalone application. I'm currently looking into ways to fix this behaviour (at least for debugging purposes)

***
### Usage
**Before using this application you have to retreive your Pebble timeline token** (you can install [this watchapp](https://apps.rebble.io/en_US/application/5d9ac26dc393f54d6b5f5445) on your Pebble - or search for "Generate Token" on the Rebble Store - and follow the instructions to get it and put it inside "token.txt")

Once it's there you can open the application and start sending pins!
***
### Future releases (may) include:
- [ ] **Pin History** - Modify already sent pins (as long as they aren't deleted by the user)
- [ ] **More Layouts** - implement all the layouts available inside the system (CalendarPin, WeatherPin, SportsPin, GenericNotification)
- [x] **More Icons** - Let the user decide from a wider selection of built-in icons
