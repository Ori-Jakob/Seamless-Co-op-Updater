@ECHO off

IF EXIST .\seamless-update.exe (
    .\seamless-update.exe
) ELSE IF EXIST .\seamless-update.py (
    python .\seamless-update.py
) ELSE (
	ECHO 'seamless-update' not found...
)



IF EXIST .\DarkSoulsIII.exe (
    SET config_name=config_darksouls3.toml
    SET launcher=ds3sc_launcher.exe
) ELSE IF EXIST .\eldenring.exe (
    SET config_name=config_eldenring.toml
    SET launcher=ersc_launcher.exe
)

IF NOT "%launcher%"=="" (

    IF EXIST .\modengine2_launcher.exe (
        ECHO Launching ModEngine2 with config file: '%config_name%'
        .\modengine2_launcher.exe -t er -c .\%config_name%
    ) ELSE IF EXIST .\%launcher% (
        ECHO Launching '%launcher%'
        .\%launcher%
    ) ELSE (
    	ECHO Could not find 'ModEngine2' or 'Seamless Co-op'
	ECHO Are they installed?
    )

) ELSE (
    ECHO Could not find 'DarkSoulsIII.exe' or 'eldenring.exe'
    ECHO Are we in the right directory?
)

timeout /t 3 >NUL