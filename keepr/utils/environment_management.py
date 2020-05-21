import subprocess
import platform
import sys
import os

from .misc_functions import is_in_venv


def check_virtualenv_exists():
    try:
        process = subprocess.Popen(['virtualenv'], stdout=subprocess.PIPE,\
             stderr=subprocess.PIPE)
        output, error = process.communicate()
        return 1
    except:
        return 0
    

def activate_env():
    if not(is_in_venv()):
        if check_virtualenv_exists():
            if platform.system() == 'Windows':
                result = subprocess.run([os.path.join('scripts', 'activate_env.bat'), r'C:\Users\HP\Desktop\Projects'],\
                     stdout=subprocess.PIPE,\
                     stderr=subprocess.PIPE)
            else:
                result = subprocess.run([os.path.join('scripts', 'activate_env.bat')],\
                     stdout=subprocess.PIPE,\
                     stderr=subprocess.PIPE)
                
                output = result.stdout.decode('utf-8')
                returncode = result.returncode
            if returncode == 0 or 'virtualenv' in output:
                print('Environment Activated!')

        else:
            print('virtualenv is not present on your system.\
                 To get this pip package follow this link https://pypi.org/project/virtualenv/')
            return
    else:
        print("Environment already activated!")
    

def deactivate_env():
    status = is_in_venv()
    if status:
        print("Deactivating environment...")
        if platform.system() == 'Windows':
            subprocess.run(["deactivate"])
        else:
            subprocess.run(["deactivate"])
        print("Environment Deactivated")
    else:
        print("No active environments")
        exit()

if __name__ == "__main__":
    activate_env()