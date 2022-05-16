import shutil
import os
import os.path
import tarfile
import wget

def download():
    print('Error')
    url = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
    file_get = wget.download(url)
    file_tar = tarfile.open('aclImdb_v1.tar.gz')
    file_tar.extractall()

def remove():
    os.remove('aclImdb_v1.tar')
    shutil.rmtree('aclImdb')

def checkIfFile():
    file_path = os.getcwd()
    # check if file exist:
    if not os.path.exists('aclImdb_v1.tar.gz'):
        download()
        print('File does not exist ')
    else:
        print('File exists')

if __name__ == '__main__':
    checkIfFile()