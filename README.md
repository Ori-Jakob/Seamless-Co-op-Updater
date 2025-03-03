# Seamless-Co-op-Updater
A simple Python script for automatically updating Seamless Co-op mod for [ELDEN RING](https://github.com/LukeYui/EldenRingSeamlessCoopRelease/) and [DARK SOULS III](https://github.com/LukeYui/DarkSouls3SeamlessCoopRelease/)

When the new update is downloaded and applied, the old configuration settings from the mod are transferred to the new one.

***Supported Games = [ ELDEN RING, DARK SOULS III ]***

# Install

### Running the seamless-update.py:

1. Make sure [Python 3](https://www.python.org/downloads/) is installed
2. Download seamless-update.py
3. Place the script in `%SUPPORTED_GAMES%/Game` folder
4. Run the script in the directory

### Running the seamless-update.exe

**_With the executable, a Python 3 runtime environment is bundled with it. Because of this, Python is NOT required to be installed for it to work_**

1. Download seamless-update.exe from [Releases](https://github.com/Ori-Jakob/Seamless-Co-op-Updater/releases/latest).
2. Place the executable in `%SUPPORTED_GAMES%/Game` folder
3. Run the executable in the directory


### Setting up Steam to launch start-with-update.bat/sh (Haven't test Linux yet)
1. Follow `Running the seamless-update.exe` or `Running the seamless-update.py`
2. Download [start-with-update.bat](https://github.com/Ori-Jakob/Seamless-Co-op-Updater/releases/latest) (Windows) or [start-with-update.sh](https://github.com/Ori-Jakob/Seamless-Co-op-Updater/releases/latest) (Linux) and place in `%SUPPORTED_GAMES%/Game` directory.
3. Open Steam, click on `Games` menu tab -> `Add a Non-Steam Game to My Library`
4. Click on `Browse` on the new winodw that pops up
5. Navigate to the game folder and select and open the script file (make sure filter is set to `All Files (*.*)` on Windows)
6. Make sure that the script is selected in the `Add a Non-Steam Game to My Library` window and click `Add Selected Programs`
7. You can now launch it through Steam and it should work it's magic

**NOTE: Linux may need more finessing to get this to work properly!**

(Optional) you can customize the app icon and name of the program by right-clicking on it in Steam and clicking `Properties`

