#!/usr/bin/python3
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

"""console"""
my_class = {"BaseModel": BaseModel, "User": User, "Place": Place,
            'Review': Review, 'Amenity': Amenity, 'State': State, 'City': City}

instance = {}


class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        'exit'
        return True

    def do_quit(self, arg):
        'exit whit command quit'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        'Create command to create a new instance'
        if not arg:
            print("** class name missing **")
        elif arg in my_class:
            for key, value in my_class.items():
                if key == arg:
                    new_class = my_class[key]()
            storage.save()
            print(new_class.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        'Prints all string representation of all instances based'
        'or not on the class name.'
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                myKey = key.split(".")
                if myKey[0] == arg[0]:
                    my_list.append(str(values))
            print(my_list)

    def do_show(self, arg):
        'Show command to show an existing instance.'
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                isFound = 0
                for key, values in my_objects.items():
                    if key == my_key:
                        isFound = 1
                        print(values)
                if isFound == 0:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                try:
                    my_objects.pop(my_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            myKei = args[0] + "." + args[1]
            isFound = 0
            for key, value in my_objects.items():
                if key == myKei:
                    isFound = 1
                    Values = my_objects.get(key)
                    setattr(value, args[2], args[3])
                    value.save()
        if isFound == 0:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
