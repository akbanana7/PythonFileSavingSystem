# Imports
import os
from time import sleep as slp
# File for file handle init
def init(): # Function for checking if datafile exists, creates one if not
    if os.path.exists("datastore.txt"):
        print("Data file found")
        return 0
    else:
        print("Data file not found")
        check = input("Would you like to create a new file? Y/N: ").lower()
        if check == "y":
            file = open("datastore.txt", "x")
            file.write("0")
            file.close()
        else:
            print("Ok exiting")
            slp(0.5)
            print("No data will be saved and python will exit with stop error")
            slp(0.5)
            print("Exiting with critical error: datafile not found: user no overwrite")
            raise Exception("Datafile not allowed")

def checkProgress(dataCheck): # Function for reading progress
    if os.path.exists("datastore.txt"):
        file = open("datastore.txt", "r")
        file.seek(0)
        toRead = file.read(1)
        print(toRead)
        file.close()
    else:
        print("Data not found")
        init()



def writeProgress(): # Function for writing progress
    if os.path.exists("datastore.txt"):
        print("Data file found.")
        file = open("datastore.txt", "w")
        file.write("0")
    else:
        init()


def newSave():
    if os.path.exists("datastore.txt"):
        os.remove("datastore.txt")
        slp(0.5)
        file = open("datastore.txt", "x")
        file.close()
        slp(0.5)
        file = open("datastore.txt", "w")
        file.write("0")
        file.close()
    else:
        file = open("datastore.txt", "x")
        file.close()
        slp(0.5)
        file = open("datastore.txt", "w")
        file.write("0")
        file.close()
        

def deleteSave():
    try:
        os.remove("datastore.txt")
    except:
        raise Exception("CRITICAL ERROR: DATAFILE NOT FOUND")