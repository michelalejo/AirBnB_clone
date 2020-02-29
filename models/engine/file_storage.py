#!usr/bin/python3
""" Store first object """
import json
from ..base_model import BaseModel
from ..amenity import Amenity
from ..city import City
from ..user import User
from ..place import Place
from ..review import Review
from ..state import State


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ Init """
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

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
        dict = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                json_file = json.loads(my_file.read())
                for key in json_file:
                    FileStorage.__objects[key] = dict[json_file[key]['__clas\
s__']](**json_file[key])
        except Exception:
            pass
