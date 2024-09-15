import subprocess, os, time, configparser





def check_dependency(package):
    try:
      return __import__(package)
    except ImportError:
      import sys
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





script_dir = os.path.dirname(os.path.realpath(__file__)) 
_sleep_duration = 5





def main():

  global _sleep_duration

  #Grab the original configuration
  original_config, new_config = configparser.ConfigParser(), configparser.ConfigParser()


  #check if original ini exists for config transfer
  if os.path.exists('./SeamlessCoop/ersc_settings.ini'):
    original_config.read('./SeamlessCoop/ersc_settings.ini') 
  else:
    original_config = None


  #Check if update exists based on previous install

  data = requests.get("https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases/latest").url[70:]
  if not checkForUpdate(data): return #don't bother running everything else if already on the latest version
  
    
  
  #Install the new update if needed
  url = 'https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases/latest/download/ersc.zip'

  print(f'Downloading Seamless Coop release {data}...')
  dload.save_unzip(url, './', delete_after=True) #unzip to root of script file
  print('Done!\n')

#update version.txt
  with open('./SeamlessCoop/version.txt', 'w') as version:
      version.write(data)


#Apply original configuration to the new configuration if old one exists
  if original_config != None:

    new_config.read('./SeamlessCoop/ersc_settings.ini')
    print('Transferring configuration file...')

    for x in new_config:
        for i in new_config[x]:
          if i in original_config[x]: #check to see if parameter exists in the original. We don't want an error for accessing an invalid parameter.
            new_config[x][i] = original_config[x][i] 

    with open('./SeamlessCoop/ersc_settings.ini', 'w') as config:
        new_config.write(config) #due to limitations of python lib configparser, comments will not be transfered to the new config

    print("Done!\n")

  else:
     print("No configuration detected. Skipping configuration transfer.")

  print('Everything Has Completed Successfully! You can launch the game now.')
     




if __name__ == "__main__":
   
  path = "ELDEN RING\\Game" if os.name == "nt" else "ELDEN RING/Game"
  
  if os.path.exists('./eldenring.exe'):
    main()
  else:
    print(f"ERROR: script is in the wrong location.'")
    print(f"The file is in the wrong path. Make sure it is placed and ran from '{path}'.")

  print(f'Exiting in {_sleep_duration} seconds...')
  time.sleep(_sleep_duration)


