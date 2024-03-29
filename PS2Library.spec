# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['app.py'],
             pathex=['env\\Lib\\site-packages', 'C:\\SoftwareDevelopment\\PS2Library'],
             binaries=[],
             datas=[('static', 'static'), ('static\\covers', 'static\\covers'), ('templates', 'templates'), ('config.ini', '.'), ('LICENSE', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PS2Library',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , uac_admin=True, icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PS2Library')
