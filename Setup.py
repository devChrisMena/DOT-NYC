import subprocess
import sys

def install(packages):
    '''
    Given a list of packages, installs packaging to the machine
    :param packages: list of packages name
    '''
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except:
            print('Could not install {}'.format(package))

def uninstall(packages):
    '''
    Given a list of packages, loops through the list to uninstall the given packages
    :param packages: list of packages name
    '''
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package])


if __name__ == "__main__":
    packages =  ['wget', 'numpy', 'panda', 'seaborn', 'matplotlib', 'jupyterlab', 'selenium', 'tensorflow', 'scikit-learn', 'kivy', 'tqdm']
    #packages_mac =  ['wget', 'numpy', 'panda', 'seaborn', 'matplotlib', 'jupyterlab', 'selenium', '--upgrade pip', 'tensorflow-metal', 'scikit-learn', 'kivy']
    install(packages)