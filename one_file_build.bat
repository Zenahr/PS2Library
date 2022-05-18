set dir="static\covers"
rmdir /s /q %dir%
mkdir %dir%
pyinstaller --name="PS2Library" --onefile --paths=env\Lib\site-packages  --add-data="templates;templates" --add-data="config.ini;." --add-data="LICENSE;." app.py --noconsole --icon=icon.ico -y
@REM mkdir "dist\static\covers"
robocopy "static" "dist\static" /E
robocopy "." "dist\" "config.ini"