import shutil
import os
import os.path
import tarfile
import wget

def download():
    '''
    Downloads sentiment library
    '''
    url = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
    file_get = wget.download(url)

def extract():
    '''
    Extracts sentiment library
    '''
    file_tar = tarfile.open('aclImdb_v1.tar.gz')
    file_tar.extractall()

def remove():
    '''
    Removes sentiment file & Directory
    '''
    os.remove('aclImdb_v1.tar')
    shutil.rmtree('aclImdb')

def checkIfFile():
    '''
    Check if sentiment library and Directory exist
    '''
    file_path = os.getcwd()
    # check if file exist:
    if not os.path.exists('aclImdb_v1.tar.gz'):
        download()
    else:
        print('File exists')

if __name__ == '__main__':
    #checkIfFile()
    extract()
