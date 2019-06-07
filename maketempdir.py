import shutil
import os
from os import listdir
from os.path import isfile, join

def maketempdir(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

    os.mkdir(path)

    aidlabel = '"PLACE FILES HERE"'
    touchcommand = "touch " + path + "/" + aidlabel
    os.system(touchcommand)

    #Specify the name of your file manager here
    filemanager = "nautilus"

    #Open folder onto screen
    folderopencommand = filemanager + " " + path

    os.system(folderopencommand)
