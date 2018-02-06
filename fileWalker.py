import os
import glob
import sys

def getFileList(path):
    # return (os.listdir(path))
    pass

def deleteFiles(list):
    pass

def Main():
    fileType = str(raw_input("Enter FileType/FileName: "))
    sourcePath = str(raw_input("Enter Path of the directory: "))
    fileList = getFileList(sourcePath)
    print fileList
    deleteFiles(fileList)

if __name__=="__main__":
    Main()