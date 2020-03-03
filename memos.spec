# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['memos.py'],
             pathex=['D:\\Feci\\RebbleMemos'],
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
a.datas += [('HOTEL_RESERVATION.png','D:\\Feci\\RebbleMemos\\assets\\HOTEL_RESERVATION.png', "DATA")]
a.datas += [('NOTIFICATION_FLAG.png','D:\\Feci\\RebbleMemos\\assets\\NOTIFICATION_FLAG.png', "DATA")]
a.datas += [('NOTIFICATION_GENERIC.png','D:\\Feci\\RebbleMemos\\assets\\NOTIFICATION_GENERIC.png', "DATA")]
a.datas += [('NOTIFICATION_REMINDER.png','D:\\Feci\RebbleMemos\\assets\\NOTIFICATION_REMINDER.png', "DATA")]
a.datas += [('SCHEDULED_EVENT.png','D:\\Feci\\RebbleMemos\\assets\\SCHEDULED_EVENT.png', "DATA")]
a.datas += [('memo.ico','D:\\Feci\\RebbleMemos\\memo.ico', "DATA")]
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
