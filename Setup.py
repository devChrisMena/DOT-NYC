import subprocess
import os
import os.path
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip3", "install", package])

def checkIfFile():
    file_path = os.getcwd()
    # check if file exist:
    if not os.path.exists('aclImdb_v1.tar.gz'):
        print('File does not exist ')
    else:
        print('File exists')

if __name__ == "__main__":
    checkIfFile()