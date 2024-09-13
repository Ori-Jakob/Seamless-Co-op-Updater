@ECHO off

IF EXIST .\seamless-update.exe (
    .\seamless-update.exe
) ELSE IF EXIST .\seamless-update.py (
    .\seamless-update.py
) ELSE (
	ECHO 'seamless-update' not found...
)


ECHO Launching game...

IF EXIST .\modengine2_launcher.exe (
    .\modengine2_launcher.exe -t er -c .\config_eldenring.toml
) ELSE (
    .\ersc_launcher.exe
)

timeout /t 2 >NUL