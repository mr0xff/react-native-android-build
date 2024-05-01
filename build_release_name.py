#!/usr/bin/env python3

from os import rename
from os import chdir
from os import system

#config build file
WORK_DIRECTORY = 'app/build/outputs/apk/release/' # you need to put this script in yout android/ directory then config your package.json file in scripts build key
CONFIG_FILE = 'output-metadata.json'
APK_FILE = 'app-release.apk'
APK_BUILD_NAME = 'my-simple-app' # change here

def main():
    chdir(WORK_DIRECTORY)
    try:
      with open(CONFIG_FILE) as file:
          version = file.readlines()[14].strip().split(':')[1].strip()
          version = '-' + version.replace('"', '').replace(',', '')
          file_build_name = APK_BUILD_NAME+ version + '.apk'
          rename(APK_FILE, file_build_name)
          system(f'cp {file_build_name} ~') # if you are windows user change this to copy command ...
          print(f'BUILD SUCCESSFUL: App builded name {file_build_name}')
          print('INFO: file copied in your home :)')  
    except Exception as err:
        print(err)

if __name__=='__main__':
    main()
