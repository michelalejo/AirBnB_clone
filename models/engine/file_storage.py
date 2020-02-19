#!usr/bin/python3
""" Store first object """
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ Constructor """
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}"
                              .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dict = {}
        """serializes __objects to the JSON file (path: __file_path)"""
        for key, value in FileStorage.__objects.items():
            dict.update({key: value.to_dict()})
            json_file = json.dumps(dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        file = ""
        try:
            with open(FileStorage.__file_path, "r") as f:
                file = json.loads(f.read())
                for key, value in file.items():
                    file.update({key: BaseModel(**value)})
                FileStorage.__objects = file
        except Exception:
            pass
