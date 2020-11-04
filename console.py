#!/usr/bin/env python3
'''Console Module =D to manipulate objects'''
import cmd
import sys
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import shlex
classes = {"BaseModel": BaseModel, "User": User, "City": City, "State": State,
           "Amenity": Amenity, "Review": Review, "Place": Place}


class HBNBCommand(cmd.Cmd):
    '''Command line interpreter class'''
    file = None

    if sys.stdin.isatty():
        intro = '----------------------------------------\n-----' + \
                ' Welcome to your HBNB Console -----\n-----     ' + \
                '  Happy Coding \o/       -----\n---------------' + \
                '-------------------------\n'
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb) \n'

    def do_quit(self, arg):
        '''quit console with quit method'''
        return True

    def do_EOF(self, arg):
        '''quit console with EOF method'''
        print()
        return True

    def emptyline(self):
        ''' empty line pass'''
        pass

    def postloop(self):
        '''postlooop goodbye'''
        Bye = '----------------------------------------\n-----' + \
            '        Come Back Soon!       -----\n-----     ' + \
            '  Have a lovely day      -----\n---------------' + \
            '-------------------------\n'
        print(Bye)

    def default(self, line):
        '''default method to cast functions'''
        arg_list = line.split('.')
        if len(arg_list) >= 2:
            if arg_list[1] == "all()":
                self.do_all(arg_list[0])
            elif arg_list[1][:4] == "show":
                self.do_show(strip_line(arg_list))
            elif arg_list[1][:7] == "destroy":
                self.do_destroy(strip_line(arg_list))
            elif arg_list[1][:6] == "update":
                self.do_update(strip_line(arg_list))

    def do_create(self, arg):
        """\n<-                    Creates a new instance:                   ->\n\
<-    Usage: create <class name>    -    Ex: create BaseModel   ->\n\
<-                 if success id will be printed                ->\n"""

        class_name = parse(arg)
        if len(class_name) == 0:
            print("** class name missing **")

        elif class_name[0] in classes:
            new_instance = classes[class_name[0]]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''shows the representation of an object'''
        line = parse(arg)
        if line == []:
            print("** class name missing **")
        elif line[0] in classes and len(line) >= 2:
            try:
                all_objs = storage.all()
                key = line[0] + "." + line[1]
                obj = all_objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        '''remove'''
        line = parse(arg)
        if line == []:
            print("** class name missing **")
        elif line[0] in classes and len(line) >= 2:
            key = line[0] + "." + line[1]
            all_objs = storage.all()
            if key in all_objs:
                storage.delete_from_objects(key)
            else:
                print("** no instance found **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        '''Prints all string representation of all instances
        based or not on the class name.'''
        line = parse(arg)
        all = storage.all()
        if line == []:
            for obj in all.values():
                print(obj)
        elif line[0] in classes:
            for keys in all:
                key = keys.split(".")[0]
                if key == line[0]:
                    print(all[keys])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        '''update method for classes'''
        line = parse(arg)
        if line == []:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif line[0] in classes:
            if len(line) == 1:
                print("** instance id missing **")
            elif len(line) >= 2:
                key = line[0] + "." + line[1]
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                elif len(line) == 2:
                    print("** attribute name missing **")
                elif len(line) == 3:
                    print("** value missing **")
                else:
                    obj = all_objs[key]
                    dict_obj = obj.to_dict()
                    dict_obj[line[2]] = line[3]
                    storage.delete_from_objects(key)
                    new_obj = classes[line[0]](**dict_obj)
                    new_obj.save()


def parse(arg):
    '''parse line from input'''
    args = shlex.split(arg)
    return args


def strip_line(case):
    '''function to parse the input line'''
    args = ""
    list1 = case
    str_class = list1[0]
    list2 = list1[1].split("(")
    str_command = list2[0]
    #   args = str_command + " "
    args = args + str_class + " "
    list3 = list2[1].split(",")
    str_id = list3[0].strip('" ()')
    args = args + str_id
    if len(list3) == 3:
        is_dict = list3[1].strip()
        if is_dict[0] == "{":
            pass
        else:
            str_atribute = list3[1].strip('" ')
            str_value = list3[2].strip('" )')
            args = args + " " + str_atribute + " "
            args = args + str_value
    return(args)


if __name__ == '__main__':
    '''main loop for console'''
    HBNBCommand().cmdloop()
