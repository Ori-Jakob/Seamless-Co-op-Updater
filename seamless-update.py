import subprocess, os, sys, time, configparser

class Game:
   def __init__(self):
      self.name = str()
      self.url = str()
      self.code = str()
      self.exe = str()
      self.mod_folder = "SeamlessCoop"
      self.found = False



def check_dependency(package):
    try:
      return __import__(package)
    except ImportError:
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])




#needs to have external library dload installed. If not installed, install it.
check_dependency('dload')
check_dependency('requests')

import requests, dload


script_dir = str()
SUPPORTED_GAMES = ["ELDEN RING", "DARK SOULS III"]

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(__file__)

_sleep_duration = 3
game = Game()


def checkForUpdate(data):

  global _sleep_duration

  if not os.path.exists(f"./{game.mod_folder}"):
      print(f"Seamless Coop not found. ")
      return True

      
  try:
    with open(f'./{game.mod_folder}/version.txt', 'r') as version:
      ver = version.readline()
      if ver == data:
        print(f"Already Updated to the latest version ({data}). Skipping Update...")
        _sleep_duration = 2
        return False

  except OSError:
    with open(f'./{game.mod_folder}/version.txt', 'w') as version:
      version.write(data)

  print(f"New update found! -> {data}")
  return True



def set_game():
  global game
  if script_dir.upper().count(os.path.join("ELDEN RING", "Game")) > 0:
    game.url = "https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases/latest"
    game.code = "er"
    game.name = "ELDEN RING"
    game.exe = "eldenring.exe"
    game.found = True
  elif script_dir.upper().count(os.path.join("ELDEN RING", "Game")) > 0:
    game.url = "https://github.com/LukeYui/DarkSouls3SeamlessCoopRelease/releases/latest"
    game.code = "ds3"
    game.name = "DARK SOULS III"
    game.exe = "DarkSoulsIII.exe"
    game.found = True
  else:
    game.name = " or ".join(["'" + os.path.join(f"{x}", "Game") + "'" for x in SUPPORTED_GAMES])



def main():

  global _sleep_duration, game

  print(f"Path = {script_dir}")
  print(f"Detected Game: {game.name}\n")
  #Grab the original configuration
  original_config, new_config = configparser.ConfigParser(), configparser.ConfigParser()


  #check if original ini exists for config transfer
  if os.path.exists(f'./{game.mod_folder}/{game.code}sc_settings.ini'):
    original_config.read(f'./{game.mod_folder}/{game.code}sc_settings.ini') 
  else:
    original_config = None


  #Check if update exists based on previous install

  data = requests.get(game.url).url[70:]
  if not checkForUpdate(data): return #don't bother running everything else if already on the latest version
  
    
  
  #Install the new update if needed
  url = f'{game.url}/download/{game.code}sc.zip'
  
  #check if the download link is valid
  try:
    requests.get(url).content.decode('utf-8') #if we can decode as uft-8 then we know it isn't a zip?
    print("ERROR: Failed to download the update.") 
    return
  except Exception:
    pass
    
  print(f'Downloading Seamless Coop release {data}...')
  
  dload.save_unzip(url, './', delete_after=True) #unzip to root of script file
  
  print('Done!\n')

#update version.txt
  with open(f'./{game.mod_folder}/version.txt', 'w') as version:
      version.write(data)


#Apply original configuration to the new configuration if old one exists
  if original_config != None:

    new_config.read(f'./{game.mod_folder}/{game.code}sc_settings.ini')
    print('Transferring configuration file...')

    for x in new_config:
        for i in new_config[x]:
          if i in original_config[x]: #check to see if parameter exists in the original. We don't want an error for accessing an invalid parameter.
            new_config[x][i] = original_config[x][i] 

    with open(f'./{game.mod_folder}/{game.code}sc_settings.ini', 'w') as config:
        new_config.write(config) #due to limitations of python lib configparser, comments will not be transfered to the new config

    print("Done!\n")

  else:
     print("No configuration detected. Skipping configuration transfer.")

  print('Everything Has completed successfully! You can launch the game now.')
     




if __name__ == "__main__":
  set_game()

  if game.found and os.path.exists(f'./{game.exe}'):
    main()
  else:
    print(f"ERROR: script is in the wrong location.")
    print(f"The file is in the wrong path. Make sure it is placed and ran from {game.name}.")

  for x in range(_sleep_duration):
    print(f'\rExiting in {_sleep_duration - x} seconds...', end="")
    time.sleep(1)
  print('\rExiting in 0 seconds...\n')