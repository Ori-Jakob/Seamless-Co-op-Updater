import subprocess, os, sys, time, configparser





def check_dependency(package):
    try:
      return __import__(package)
    except ImportError:
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])




#needs to have external library dload installed. If not installed, install it.
check_dependency('dload')
check_dependency('requests')

import requests, dload





def checkForUpdate(data):

  global _sleep_duration

  if not os.path.exists("./SeamlessCoop"):
      print(f"Seamless Coop not found. ")
      return True

      
  try:
    with open('./SeamlessCoop/version.txt', 'r') as version:
      ver = version.readline()
      if ver == data:
        print(f"Already Updated to the latest version ({data}). Skipping Update...")
        _sleep_duration = 2
        return False

  except OSError:
    with open('./SeamlessCoop/version.txt', 'w') as version:
      version.write(data)

  print(f"New update found! -> {data}")
  return True





script_dir = str()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(__file__)

_sleep_duration = 5
game = dict()

def set_game():
  global game
  if script_dir.upper().count("ELDEN RING") > 0:
    game = {
      "url": "https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases/latest",
      "code": "er",
      "name": "ELDEN RING",
      "exe": "eldenring.exe"
    }
  else:
    game = {
      "url": "https://github.com/LukeYui/DarkSouls3SeamlessCoopRelease/releases/latest",
      "code": "ds3",
      "name": "DARK SOULS III",
      "exe": "DarkSoulsIII.exe"
    }



def main():

  global _sleep_duration, game
  print(script_dir)
  print(f"Detected Game: {game["name"]}\n")
  #Grab the original configuration
  original_config, new_config = configparser.ConfigParser(), configparser.ConfigParser()


  #check if original ini exists for config transfer
  if os.path.exists(f'./SeamlessCoop/{game["code"]}sc_settings.ini'):
    original_config.read(f'./SeamlessCoop/{game["code"]}sc_settings.ini') 
  else:
    original_config = None


  #Check if update exists based on previous install

  data = requests.get(game["url"]).url[70:]
  if not checkForUpdate(data): return #don't bother running everything else if already on the latest version
  
    
  
  #Install the new update if needed
  url = f'{game["url"]}/download/ersc.zip'

  print(f'Downloading Seamless Coop release {data}...')
  dload.save_unzip(url, './', delete_after=True) #unzip to root of script file
  print('Done!\n')

#update version.txt
  with open('./SeamlessCoop/version.txt', 'w') as version:
      version.write(data)


#Apply original configuration to the new configuration if old one exists
  if original_config != None:

    new_config.read(f'./SeamlessCoop/{game["code"]}sc_settings.ini')
    print('Transferring configuration file...')

    for x in new_config:
        for i in new_config[x]:
          if i in original_config[x]: #check to see if parameter exists in the original. We don't want an error for accessing an invalid parameter.
            new_config[x][i] = original_config[x][i] 

    with open(f'./SeamlessCoop/{game["code"]}sc_settings.ini', 'w') as config:
        new_config.write(config) #due to limitations of python lib configparser, comments will not be transfered to the new config

    print("Done!\n")

  else:
     print("No configuration detected. Skipping configuration transfer.")

  print('Everything Has Completed Successfully! You can launch the game now.')
     




if __name__ == "__main__":
  set_game()
  path = f"{game["name"]}\\Game" if os.name == "nt" else f"{game["name"]}/Game"
  
  if os.path.exists(f'./{game["exe"]}'):
    main()
  else:
    print(f"ERROR: script is in the wrong location.'")
    print(f"The file is in the wrong path. Make sure it is placed and ran from '{path}'.")

  print(f'Exiting in {_sleep_duration} seconds...')
  time.sleep(_sleep_duration)