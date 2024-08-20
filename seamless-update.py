import subprocess, os, time

def check_dependency(package):
    try:
      return __import__(package)
    except ImportError:
      import sys
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

check_dependency('dload')


import configparser, dload

script_dir = os.path.dirname(os.path.realpath(__file__))
sleep_duration = 5

def main():

  #Grab the original configuration
  original_config, new_config = configparser.ConfigParser(), configparser.ConfigParser()


  #check if original ini exists for config transfer
  if os.path.exists('./SeamlessCoop/ersc_settings.ini'):
    original_config.read('./SeamlessCoop/ersc_settings.ini') 
  else:
    original_config = None


  #Install the new update
  url = 'https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases/latest/download/ersc.zip'
  print('Downloading Latest Update...')
  dload.save_unzip(url, './', delete_after=True) #unzip to root of script file
  print('Done!\n')


  #Apply original configuration to the new configuration if old one exists
  if original_config != None:

    new_config.read('./SeamlessCoop/ersc_settings.ini')
    print('Transferring configuration file...')


    for x in new_config:
        for i in new_config[x]:
          if i in original_config[x]: #check to see if parameter exists in the original. We don't want an error!
            new_config[x][i] = original_config[x][i] 

    with open('./SeamlessCoop/ersc_settings.ini', 'w') as config:
        new_config.write(config) #due to limitations of the configparser, comments will not be transfered to the new config
    print("Done!\n")
  else:
     print("No configuration detected. Skipping configuration transfer.")

  print('Everything Has Completed Successfully! You can launch the game now.')
     

if __name__ == "__main__":
   
  path = "ELDEN RING\\Game" if os.name == "nt" else "ELDEN RING/Game"
  
  if os.path.exists('./eldenring.exe'):
    main()
  else:
    print(f"ERROR: Current script location -> '{script_dir}'")
    print(f"The file is in the wrong path. Make sure it is placed and ran from '{path}'.")

  print(f'Exiting in {sleep_duration} seconds...')
  time.sleep(sleep_duration)


