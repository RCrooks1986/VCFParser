import shutil
import os
from os import listdir
from os.path import isfile, join

def maketempdir(path):
    #Make folder if does not already exist
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)

    #Make file saying put in folder
    aidlabel = '"PLACE FILES HERE"'
    touchcommand = "touch " + path + "/" + aidlabel
    os.system(touchcommand)
