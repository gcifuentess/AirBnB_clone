#!/usr/bin/python3
"""Console Test Module"""
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand
from console import classes


class ConsoleTest(unittest.TestCase):
    '''Class to test the Console'''

    str_id = "None"
    my_class = 'BaseModel'  # list(classes.keys())[0]

    def test_00_help(self):
        '''Checks the help command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            str_test = f.getvalue().rstrip()
        str_exp = HBNBCommand.do_show.__doc__
        self.assertEqual(str_test, str_exp)

    def test_01_create(self):
        '''Checks the create command'''

        # checks the command without args
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            str_test = f.getvalue().rstrip()

        str_exp = "** class name missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with a non existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create " + self.my_class)
            str_test = f.getvalue().rstrip()

        exp_len = 36  # the total len of the id
        exp_sublen = 4  # len of time_mid, time_hi_version, etc fields of id
        str_test_len = len(str_test)
        str_test_split = str_test.split('-')
        if str_test_len == exp_len:
            ConsoleTest.str_id = str_test  # id going to be used in other tests

        # -- to validate the correct structure of the id
        self.assertEqual(str_test_len, exp_len)
        self.assertEqual(len(str_test_split[1]), exp_sublen)
        self.assertEqual(len(str_test_split[2]), exp_sublen)
        self.assertEqual(len(str_test_split[3]), exp_sublen)

    def test_02_show(self):
        '''Checks the show command'''

        # checks the command without args
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            str_test = f.getvalue().rstrip()

        str_exp = "** class name missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with a non existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname and no id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + self.my_class)
            str_test = f.getvalue().rstrip()

        str_exp = "** instance id missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname with an id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + self.my_class + " " + self.str_id)
            str_test = f.getvalue().rstrip()

        split = str_test.split()
        str_test_class = split[0].lstrip("[").rstrip("]")
        str_test_id = split[1].lstrip("(").rstrip(")")

        self.assertEqual(str_test_class, self.my_class)
        self.assertEqual(str_test_id, self.str_id)

        # checks the command with an existing classname with a non existing id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + self.my_class + " " + "1234")
            str_test = f.getvalue().rstrip()

        str_exp = "** no instance found **"
        self.assertEqual(str_test, str_exp)

    def test_03_destroy(self):
        '''Checks the destroy command'''

        # checks the command without args
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            str_test = f.getvalue().rstrip()

        str_exp = "** class name missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with a non existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname and no id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy " + self.my_class)
            str_test = f.getvalue().rstrip()

        str_exp = "** instance id missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname with a non existing id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy " + self.my_class + " " + "1234")
            str_test = f.getvalue().rstrip()

        str_exp = "** no instance found **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname with an id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy " + self.my_class + " "+self.str_id)
            HBNBCommand().onecmd("show " + self.my_class + " " + self.str_id)
            str_test = f.getvalue().rstrip()

        str_exp = "** no instance found **"
        self.assertEqual(str_test, str_exp)

    def test_04_all(self):
        '''Checks the all command'''

        # checks the command without args
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            str_test = f.getvalue().rstrip()

        my_dict = storage.all()
        exp_len = 0
        for value in my_dict.values():
            exp_len += len(str(value)) + 1
        if exp_len > 0:
            exp_len -= 1
        len_str_test = len(str_test)

        # the output of all is validated through the len of str
        self.assertEqual(len_str_test, exp_len)

        # checks the command with a non existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all " + self.my_class)
            str_test = f.getvalue().rstrip()

        my_dict = storage.all()
        exp_len = 0
        for key, value in my_dict.items():
            key = key.split('.')[0]
            if key == self.my_class:
                exp_len += len(str(value)) + 1
        if exp_len > 0:
            exp_len -= 1
        len_str_test = len(str_test)

        # the output of all is validated through the len of str
        self.assertEqual(len_str_test, exp_len)

    def test_05_update(self):
        '''Checks the update command'''

        # checks the command without args
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            str_test = f.getvalue().rstrip()

        str_exp = "** class name missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with a non existing classname
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update test")
            str_test = f.getvalue().rstrip()

        str_exp = "** class doesn't exist **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname and no id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class)
            str_test = f.getvalue().rstrip()

        str_exp = "** instance id missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname with a non existing id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class + " " + "1234")
            str_test = f.getvalue().rstrip()

        str_exp = "** no instance found **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname
        #     with a valid id and no argument
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create " + self.my_class)
            str_test_id = f.getvalue().rstrip()
            ConsoleTest.str_id = str_test_id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class + " " + self.str_id)
            str_test = f.getvalue().rstrip()

        str_exp = "** attribute name missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname
        #     with a valid id, valid argument and no value
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class + " " +
                                 self.str_id + " name")
            str_test = f.getvalue().rstrip()

        str_exp = "** value missing **"
        self.assertEqual(str_test, str_exp)

        # checks the command with an existing classname
        #     with a valid id, valid argument and a valid value
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class + " "+self.str_id +
                                 " Fullname " + '"Betty Holberton"')
            str_test = f.getvalue().rstrip()

        key = self.my_class + "." + self.str_id
        test_dict = storage.all()
        obj = test_dict[key]
        obj_dict = obj.to_dict()

        exp_date = obj.created_at
        test_date = obj.updated_at

        self.assertNotEqual(test_date, exp_date)
        self.assertTrue('Fullname' in obj_dict)
        self.assertTrue("Betty Holberton" in obj_dict.values())

        # checks the command with an existing classname
        #     with a valid id, valid argument, a valid value and only
        #     updates one atribute
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + self.my_class + " "+self.str_id +
                                 " Fullname " + '"Betty Holberton"' + " age " +
                                 "52")
            str_test = f.getvalue().rstrip()

        key = self.my_class + "." + self.str_id
        test_dict = storage.all()
        obj = test_dict[key]
        obj_dict = obj.to_dict()

        exp_date = obj.created_at
        test_date = obj.updated_at

        self.assertNotEqual(test_date, exp_date)
        self.assertTrue('Fullname' in obj_dict)
        self.assertTrue("Betty Holberton" in obj_dict.values())
        self.assertFalse('age' in obj_dict)
        self.assertFalse("52" in obj_dict.values())
