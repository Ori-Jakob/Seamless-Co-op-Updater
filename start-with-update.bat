@ECHO off

IF EXIST .\seamless-update.exe (
    .\seamless-update.exe
) ELSE (
    .\seamless-update.py
)


ECHO Launching game...

IF EXIST .\modengine2_launcher.exe (
    .\modengine2_launcher.exe -t er -c .\config_eldenring.toml
) ELSE (
    .\ersc_launcher.exe
)

timeout /t 2 >NUL