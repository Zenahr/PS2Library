set dir="static\covers"
rmdir /s /q %dir%
mkdir %dir%
pyinstaller --name="PS2Library" --paths=env\Lib\site-packages --add-data="static;static" --add-data="static\covers;static\covers" --add-data="templates;templates" --add-data="config.ini;." --add-data="LICENSE;." app.py --noconsole --icon=icon.ico --uac-admin -y
mkdir "dist\PS2Library\static\covers"