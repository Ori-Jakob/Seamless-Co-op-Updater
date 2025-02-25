#!/bin/bash

# Check for seamless-update and run it if found
if [[ -f ./seamless-update.exe ]]; then
    ./seamless-update.exe
elif [[ -f ./seamless-update.py ]]; then
    python3 ./seamless-update.py
else
    echo "'seamless-update' not found..."
fi

echo
echo "Launching game..."

# Determine game configuration
if [[ -f ./DarkSoulsIII.exe ]]; then
    config_name="config_darksouls3.toml"
    launcher="ds3sc_launcher.exe"
elif [[ -f ./eldenring.exe ]]; then
    config_name="config_eldenring.toml"
    launcher="ersc_launcher.exe"
else
    launcher=""
fi

# Launch the appropriate program
if [[ -n "$launcher" ]]; then
    if [[ -f ./modengine2_launcher.exe ]]; then
        echo "Launching ModEngine2 with config file: '$config_name'"
        ./modengine2_launcher.exe -t er -c ./"$config_name"
    elif [[ -f ./"$launcher" ]]; then
        echo "Launching '$launcher'"
        ./"$launcher"
    fi
else
    echo "Could not find 'ModEngine2' or 'Seamless Co-op'"
    echo "Are we in the right directory?"
fi

# Wait for 2 seconds before exiting
sleep 2
