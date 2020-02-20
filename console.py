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
                    instance = my_class[key]()
            storage.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        'Show all instances based on class name.'
        args = arg.split(" ")
        if not arg:
            List = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                List.append(str(values))
            print(List)
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        else:
            List = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                Key = key.split(".")
                if Key[0] == args[0]:
                    List.append(str(values))
            print(List)

    def do_show(self, arg):
        'Show command to show an existing instance.'
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        elif len(args) >= 1:
            try:
                my_objects = FileStorage.all(self)
                Key = args[0] + "." + args[1]
                isFound = 0
                for key, values in my_objects.items():
                    if key == Key:
                        isFound = 1
                        print(values)
                if isFound == 0:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        elif len(args) >= 1:
            try:
                my_objects = FileStorage.all(self)
                Key = args[0] + "." + args[1]
                try:
                    my_objects.pop(Key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            Key = args[0] + "." + args[1]
            isFound = 0
            for key, values in my_objects.items():
                if key == Key:
                    isFound = 1
                    my_values = my_objects.get(key)
                    setattr(values, args[2], args[3])
                    values.save()
            if isFound == 0:
                print("** no instance found **")

    def do_User(self, arg):
        'retrieve all instances of a class by using'
        the_class = "User"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_BaseModel(self, arg):
        'retrieve all instances of a class by using'
        the_class = "BaseModel"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_State(self, arg):
        'retrieve all instances of a class by using'
        the_class = "State"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_City(self, arg):
        'retrieve all instances of a class by using'
        the_class = "City"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_Amenity(self, arg):
        'retrieve all instances of a class by using'
        the_class = "Amenity"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_Place(self, arg):
        'retrieve all instances of a class by using'
        the_class = "Place"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_Review(self, arg):
        'retrieve all instances of a class by using'
        the_class = "Review"
        args = arg.split(".")
        if args[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif args[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            first = args[1].find('("')
            second = args[1].find('")')
            args1 = args[1][0:first]
            args2 = args[1][first + 2: second]
            if args1 == "show":
                params = the_class + " " + args2
                HBNBCommand.do_show(HBNBCommand, params)

    def do_count(self, arg):
        'retrieve the number of instances of a class'
        count = 0
        args = arg.split(" ")
        if not arg:
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                List.append(str(values))
            print(List)
        elif args[0] not in my_class:
            print("** class doesn't exist **")
        else:
            List = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                Key = key.split(".")
                if Key[0] == args[0]:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
