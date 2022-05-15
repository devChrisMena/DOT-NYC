import subprocess
import os
import os.path
import sys
import tarfile

def install(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def checkIfFile():
    file_path = os.getcwd()
    # check if file exist:
    if not os.path.exists('aclImdb_v1.tar.gz'):
        print('File does not exist ')
    else:
        print('File exists')

def download():
    try:
        import wget
    except:
        print('Error')
    url = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
    file_get = wget.download(url)
    file_tar = tarfile.open('aclImdb_v1.tar.gz')
    file_tar.extractall()

if __name__ == "__main__":
    packages =  ['wget', 'numpy', 'panda', 'seaborn', 'matplotlib', 'jupyterlab', 'selenium', 'tensorflow', 'scikit-learn', 'kivy']
    install(packages)