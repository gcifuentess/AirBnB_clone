#!/usr/bin/python3
'''File Storage module '''
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Reloads file from disk"""
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
        except FileNotFoundError:
            return
        for key, value in data.items():
            eval(key.split(".")[0] + '(**value)')

    def delete_from_objects(self, key):
        '''remove an object from objects & save updated file.json'''
        if key in self.__objects:
            del self.__objects[key]
        self.save()

    def class_attributes(self):
        '''returns a dict with all models attibutes'''

        attrbs = {'BaseModel': {'id': str, 'created_at': datetime.datetime,
                                'updated_at': datetime.datetime},

                  'User': {'email': str, 'password': str, 'first_name': str,
                           'last_name': str},

                  'State': {'name': str},

                  'City': {'state_id': str, 'name': str},

                  'Amenity': {'name': str},

                  'Place': {'city_id': str, 'user_id': str, 'name': str,
                            'description': str, 'number_rooms': int,
                            'number_bathrooms': int, 'max_guest': int,
                            'price_by_night': int, 'latitude': float,
                            'longitude': float, 'amenity_ids': list},

                  'Review': {'place_id': str, 'user_id': str, 'text': str}}

        return attrbs
