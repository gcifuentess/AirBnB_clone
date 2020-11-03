#!/usr/bin/python3
"""File Storage Class Test Module"""
import unittest
import json
from models import storage
from models.base_model import BaseModel


class FileStorageTest(unittest.TestCase):
    '''Class to test the File Storage Class'''

    def test_00_all_method(self):
        '''checks if class method all returns a dict'''
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)
        # self.assertEqual(all_objs, {})

    def test_01_objects_not_empty(self):
        '''checks if class attribute __objects fills after model instance'''
        my_model = BaseModel()
        my_model.name = "test_01"
        my_model.my_number = 1
        all_objs = storage.all()

        # check if __objects is not empty
        self.assertNotEqual(all_objs, {})

        # check the correct key of the object
        my_key = str(type(my_model).__name__) + "." + str(my_model.id)
        self.assertTrue(my_key in all_objs.keys())

    def test_02_serialization(self):
        '''checks the correct serialization of an object'''
        my_model = BaseModel()
        my_model.name = "test_02"
        my_model.my_number = 2
        my_model.save()

        my_key = str(type(my_model).__name__) + "." + str(my_model.id)

        json_file = "file.json"  # storage.__file_path
        with open(json_file, "r", encoding='utf-8') as f:
            json_dict = json.load(f)

        exp_dict = json_dict[my_key]
        self.assertEqual(my_model.to_dict(), exp_dict)

    def test_03_deserialization(self):
        '''checks the correct deserialization of an object'''

        # this test depends on test_02_serialization
        # the json file must be present in the directory
        storage.reload()  # here happens the deserialization
        all_objs = storage.all()
        test_obj = list(all_objs.values())[0]
        my_key = str(type(test_obj).__name__) + "." + str(test_obj.id)

        json_file = "file.json"  # storage.__file_path
        with open(json_file, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
        exp_dict = json_dict[my_key]

        self.assertEqual(test_obj.to_dict(), exp_dict)
