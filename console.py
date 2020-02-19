#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

"""console"""


class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
