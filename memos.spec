# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['memos.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('ALARM_CLOCK.png','assets\\ALARM_CLOCK.png', "DATA")]
a.datas += [('AMERICAN_FOOTBALL.png','assets\\AMERICAN_FOOTBALL.png', "DATA")]
a.datas += [('AUDIO_CASSETTE.png','assets\\AUDIO_CASSETTE.png', "DATA")]
a.datas += [('BASKETBALL.png','assets\\BASKETBALL.png', "DATA")]
a.datas += [('BIRTHDAY_EVENT.png','assets\\BIRTHDAY_EVENT.png', "DATA")]
a.datas += [('CAR_RENTAL.png','assets\\CAR_RENTAL.png', "DATA")]
a.datas += [('CLOUDY_DAY.png','assets\\CLOUDY_DAY.png', "DATA")]
a.datas += [('CRICKET_GAME.png','assets\\CRICKET_GAME.png', "DATA")]
a.datas += [('DINNER_RESERVATION.png','assets\\DINNER_RESERVATION.png', "DATA")]
a.datas += [('DISMISSED_PHONE_CALL.png','assets\\DISMISSED_PHONE_CALL.png', "DATA")]
a.datas += [('GENERIC_CONFIRMATION.png','assets\\GENERIC_CONFIRMATION.png', "DATA")]
a.datas += [('GENERIC_EMAIL.png','assets\\GENERIC_EMAIL.png', "DATA")]
a.datas += [('GENERIC_QUESTION.png','assets\\GENERIC_QUESTION.png', "DATA")]
a.datas += [('GENERIC_WARNING.png','assets\\GENERIC_WARNING.png', "DATA")]
a.datas += [('GLUCOSE_MONITOR.png','assets\\GLUCOSE_MONITOR.png', "DATA")]
a.datas += [('HEAVY_RAIN.png','assets\\HEAVY_RAIN.png', "DATA")]
a.datas += [('HEAVY_SNOW.png','assets\\HEAVY_SNOW.png', "DATA")]
a.datas += [('HOCKEY_GAME.png','assets\\HOCKEY_GAME.png', "DATA")]
a.datas += [('INCOMING_PHONE_CALL.png','assets\\INCOMING_PHONE_CALL.png', "DATA")]
a.datas += [('LIGHT_RAIN.png','assets\\LIGHT_RAIN.png', "DATA")]
a.datas += [('LIGHT_SNOW.png','assets\\LIGHT_SNOW.png', "DATA")]
a.datas += [('LOCATION.png','assets\\LOCATION.png', "DATA")]
a.datas += [('MOVIE_EVENT.png','assets\\MOVIE_EVENT.png', "DATA")]
a.datas += [('MUSIC_EVENT.png','assets\\MUSIC_EVENT.png', "DATA")]
a.datas += [('NEWS_EVENT.png','assets\\NEWS_EVENT.png', "DATA")]
a.datas += [('NOTIFICATION_LIGHTHOUSE.png','assets\\NOTIFICATION_LIGHTHOUSE.png', "DATA")]
a.datas += [('PARTLY_CLOUDY.png','assets\\PARTLY_CLOUDY.png', "DATA")]
a.datas += [('PAY_BILL.png','assets\\PAY_BILL.png', "DATA")]
a.datas += [('RADIO_SHOW.png','assets\\RADIO_SHOW.png', "DATA")]
a.datas += [('RAINING_AND_SNOWING.png','assets\\RAINING_AND_SNOWING.png', "DATA")]
a.datas += [('REACHED_FITNESS_GOAL.png','assets\\REACHED_FITNESS_GOAL.png', "DATA")]
a.datas += [('RESULT_DISMISSED.png','assets\\RESULT_DISMISSED.png', "DATA")]
a.datas += [('RESULT_FAILED.png','assets\\RESULT_FAILED.png', "DATA")]
a.datas += [('SCHEDULED_FLIGHT.png','assets\\SCHEDULED_FLIGHT.png', "DATA")]
a.datas += [('SETTINGS.png','assets\\SETTINGS.png', "DATA")]
a.datas += [('SOCCER_GAME.png','assets\\SOCCER_GAME.png', "DATA")]
a.datas += [('STOCKS_EVENT.png','assets\\STOCKS_EVENT.png', "DATA")]
a.datas += [('SUNRISE.png','assets\\SUNRISE.png', "DATA")]
a.datas += [('SUNSET.png','assets\\SUNSET.png', "DATA")]
a.datas += [('TIDE_IS_HIGH.png','assets\\TIDE_IS_HIGH.png', "DATA")]
a.datas += [('TIMELINE_BASEBALL.png','assets\\TIMELINE_BASEBALL.png', "DATA")]
a.datas += [('TIMELINE_MISSED_CALL.png','assets\\TIMELINE_MISSED_CALL.png', "DATA")]
a.datas += [('TIMELINE_CALENDAR.png','assets\\TIMELINE_CALENDAR.png', "DATA")]
a.datas += [('TIMELINE_SPORTS.png','assets\\TIMELINE_SPORTS.png', "DATA")]
a.datas += [('TIMELINE_SUN.png','assets\\TIMELINE_SUN.png', "DATA")]
a.datas += [('TIMELINE_WEATHER.png','assets\\TIMELINE_WEATHER.png', "DATA")]
a.datas += [('TV_SHOW.png','assets\\TV_SHOW.png', "DATA")]
a.datas += [('HOTEL_RESERVATION.png','assets\\HOTEL_RESERVATION.png', "DATA")]
a.datas += [('NOTIFICATION_FLAG.png','assets\\NOTIFICATION_FLAG.png', "DATA")]
a.datas += [('NOTIFICATION_GENERIC.png','assets\\NOTIFICATION_GENERIC.png', "DATA")]
a.datas += [('NOTIFICATION_REMINDER.png','assets\\NOTIFICATION_REMINDER.png', "DATA")]
a.datas += [('SCHEDULED_EVENT.png','assets\\SCHEDULED_EVENT.png', "DATA")]
a.datas += [('memo.ico','memo.ico', "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Rebble Memos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
