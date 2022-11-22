from .utilities import *
import json
import os


class Yoda:
    """
    This class takes a path to a JSON file and loads its contents.
    If the JSON file doesn't exist, it will construct the JSON file, save it and still get the required contents

    For some reason I was running this in python 2.7, note that it does not work in 2.7
    """
    def __init__(self, path, keys=None):
        if keys is None:
            keys = []
        self.path = path
        self.keys = keys  # used for when the JSON doesn't exist and constructs a json with these values
        self.contents()

    def contents(self):
        contents = self.__open()
        if contents == {}:
            contents = self.__createJSON()
        return contents

    def __createJSON(self):
        titles = self.keys
        contents = {}
        if len(titles) > 0:
            print("For each key, give its required value")
        for title in titles:
            try:
                value = str(input("{}: ".format(title)))
            except NameError:
                value = ":("
                print("You are not running python 3!")
            contents[title] = value

        self.write(contents)
        return contents

    def __open(self):
        path = self.getPath()
        try:
            jsonFile = open(path)
            file = json.load(jsonFile)
            jsonFile.close()
            return file
        except IOError:
            if ".json" not in path:  # try opening the json file with .json
                self.__setPath(path + ".json")
                return self.__open()
            else:
                return {}
        except ValueError:
            return {}

    def write(self, contents):
        assert type(contents) is dict
        path = self.getPath()
        try:
            jsonFile = open(path, "w")
        except FileNotFoundError:
            # If Yoda has to create the dirs that are required
            dirPath = os.path.dirname(path)
            os.makedirs(dirPath)
            jsonFile = open(path, "w")
        json.dump(contents, jsonFile, indent=4)
        jsonFile.close()
        return True

    def delete(self):
        if os.path.exists(self.getPath()):
            os.remove(self.getPath())
            return True
        return False

    def getCreationTime(self):
        if os.path.exists(self.getPath()):
            unixTimestamp = os.path.getctime(self.getPath())
            return unixToDatetime(unixTimestamp)
        return None

    def getModificationTime(self):
        if os.path.exists(self.getPath()):
            unixTimestamp = os.path.getmtime(self.getPath())
            return unixToDatetime(unixTimestamp)
        return None

    def getPath(self):
        return self.path

    def __setPath(self, path):
        if self.path != path:
            self.path = path
            return True
        return False

