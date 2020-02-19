#!/usr/bin/python3
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

"""console"""


class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = '(hbnb) '
    my_class = ['BaseModel', 'User', 'Place', 'Review',
                'Amenity', 'State', 'City']

    def do_EOF(self, line):
        'exit'
        return True

    def do_quit(self, line):
        'exit whit command quit'
        return True

    def emptyline(self):
        'Empty line'
        return ""

    def do_create(self, arg):
        'Create command to create a new instance'
        if not arg:
            print("** class name missing **")
        elif arg in self.my_class:
            obj = BaseModel()
            storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        'Prints all string representation of all instances based'
        'or not on the class name.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)

    def do_show(self, arg):
        'Show command to show an existing instance.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 2:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            isFound = 0
            for key, values in my_objects.items():
                if key == my_key:
                    isFound = 1
                    print(values)
            if isFound == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
