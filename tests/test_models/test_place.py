#!/usr/bin/python3
"""City Class Test Module"""
import unittest
from datetime import timedelta  # for isoformat and fromisoformat
from datetime import datetime  # for strftime
from datetime import date
import uuid
from models.place import Place
from models.base_model import BaseModel


class PlaceTest(unittest.TestCase):
    '''Class to test the Place Class'''

    def test_00_id(self):
        '''If the id of the an instance is correct'''

        my_model_0 = Place()
        my_model_1 = Place()
        my_model_2 = Place()

        # 1) check if id len is 36 including '-'
        self.assertEqual(len(my_model_0.id), 36)
        self.assertEqual(len(my_model_1.id), 36)
        self.assertEqual(len(my_model_2.id), 36)

        # 2) check if the type of the id is str
        self.assertEqual(type(my_model_0.id), str)
        self.assertEqual(type(my_model_1.id), str)
        self.assertEqual(type(my_model_2.id), str)

        # 3) check if all id's are different
        self.assertNotEqual(my_model_0.id, my_model_1.id)
        self.assertNotEqual(my_model_0.id, my_model_2.id)
        self.assertNotEqual(my_model_1.id, my_model_2.id)

    def test_1_created_at(self):
        '''If the date of creation of the instance is correct'''

        my_model_0 = Place()
        my_model_1 = Place()
        my_model_2 = Place()

        # 1) Checks if the creation date is a datetime object
        self.assertEqual(type(my_model_0.created_at), datetime)
        self.assertEqual(type(my_model_1.created_at), datetime)
        self.assertEqual(type(my_model_2.created_at), datetime)

        # 2) Checks if when an instance is created, created_at == updated_at
        self.assertEqual(my_model_0.created_at, my_model_0.updated_at)
        self.assertEqual(my_model_1.created_at, my_model_1.updated_at)
        self.assertEqual(my_model_2.created_at, my_model_2.updated_at)

        # 3) Checks if creation date is set with the creation of the instance
        actual_date = datetime.now()
        time_spread = timedelta(seconds=1)

        self.assertTrue(actual_date - my_model_0.created_at < time_spread)
        self.assertTrue(actual_date - my_model_1.created_at < time_spread)
        self.assertTrue(actual_date - my_model_2.created_at < time_spread)

    def test_2_updated_at_and_save(self):
        '''If updated_at works when save() is called'''

        my_model_0 = Place()
        my_model_1 = Place()
        my_model_2 = Place()

        # 1) Checks if when an instance is updated, created_at != updated_at
        my_model_0.save()
        my_model_1.save()
        my_model_2.save()

        self.assertNotEqual(my_model_0.created_at, my_model_0.updated_at)
        self.assertNotEqual(my_model_1.created_at, my_model_1.updated_at)
        self.assertNotEqual(my_model_2.created_at, my_model_2.updated_at)

        # 2) Checks if update date is actual
        my_model_0.save()
        my_model_1.save()
        my_model_2.save()

        actual_date = datetime.now()
        time_spread = timedelta(seconds=1)

        self.assertTrue(actual_date - my_model_0.updated_at < time_spread)
        self.assertTrue(actual_date - my_model_1.updated_at < time_spread)
        self.assertTrue(actual_date - my_model_2.updated_at < time_spread)

    def test_3_str(self):
        '''If str method work as expected'''

        my_model_0 = Place()
        my_model_1 = Place()
        my_model_2 = Place()

        str_model_0 = "[" + str(type(my_model_0).__name__) + "] (" + \
                      str(my_model_0.id) + ") " + str(my_model_0.__dict__)
        str_model_1 = "[" + str(type(my_model_1).__name__) + "] (" + \
                      str(my_model_1.id) + ") " + str(my_model_1.__dict__)
        str_model_2 = "[" + str(type(my_model_2).__name__) + "] (" + \
                      str(my_model_2.id) + ") " + str(my_model_2.__dict__)

        self.assertEqual(str(my_model_0), str_model_0)
        self.assertEqual(my_model_1.__str__(), str_model_1)
        self.assertEqual(my_model_2.__str__(), str_model_2)

    def test_4_to_dict(self):
        '''If to_dict method work correctly'''

        my_model_0 = Place()
        my_model_1 = Place()
        my_model_2 = Place()

        dict_0 = my_model_0.to_dict()
        dict_1 = my_model_1.to_dict()
        dict_2 = my_model_2.to_dict()

        # 1) Checks if is a dictionary
        self.assertEqual(type(dict_0), dict)
        self.assertEqual(type(dict_1), dict)
        self.assertEqual(type(dict_2), dict)

        # 2) Checks if the creation date is in ISO 8601 format
        date_0 = my_model_0.created_at
        date_1 = my_model_1.created_at
        date_2 = my_model_2.created_at

        str_date_0 = date_0.strftime("%Y-%m-%dT%H:%M:%S.%f")
        str_date_1 = date_1.strftime("%Y-%m-%dT%H:%M:%S.%f")
        str_date_2 = date_2.strftime("%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(dict_0['created_at'], str_date_0)
        self.assertEqual(dict_1['created_at'], str_date_1)
        self.assertEqual(dict_2['created_at'], str_date_2)

        # 3) Checks if the update date is in ISO 8601 format
        date_0 = my_model_0.updated_at
        date_1 = my_model_1.updated_at
        date_2 = my_model_2.updated_at

        str_date_0 = date_0.strftime("%Y-%m-%dT%H:%M:%S.%f")
        str_date_1 = date_1.strftime("%Y-%m-%dT%H:%M:%S.%f")
        str_date_2 = date_2.strftime("%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(dict_0['created_at'], str_date_0)
        self.assertEqual(dict_1['created_at'], str_date_1)
        self.assertEqual(dict_2['created_at'], str_date_2)

        # 4) Checks if the __class__ is in dict

        class_0 = type(my_model_0).__name__
        class_1 = type(my_model_1).__name__
        class_2 = type(my_model_2).__name__

        self.assertEqual(dict_0['__class__'], class_0)
        self.assertEqual(dict_1['__class__'], class_1)
        self.assertEqual(dict_2['__class__'], class_2)

    def test_5_kwargs(self):
        '''If object is correctly created with kwargs'''

        my_id = str(uuid.uuid4())
        actual_date = datetime.now().isoformat()
        Mod1 = Place(id=my_id, created_at=actual_date,
                     updated_at=actual_date, __class__='Place',
                     test='my_test')
        self.assertTrue(isinstance(Mod1, Place))
        self.assertEqual(str, type(Mod1.id))
        self.assertEqual(datetime, type(Mod1.created_at))
        self.assertEqual(datetime, type(Mod1.updated_at))

        # Check that __class__ atribute is not created
        self.assertFalse('__class__' in Mod1.__dict__)

        # Check if a custom atribute is created
        self.assertTrue('test' in Mod1.__dict__)
        self.assertTrue('my_test' in Mod1.__dict__.values())

    def test_6_Place_class(self):
        '''If object is correctly a Place instance'''

        my_model_0 = Place()

        self.assertTrue(type(my_model_0) == Place)

    def test_7_BaseModel_child(self):
        '''If object is correctly a BaseModel child'''

        my_model_0 = Place()

        self.assertTrue(issubclass(type(my_model_0), BaseModel) and
                        type(my_model_0) != BaseModel)

    def test_8_Place_type_args(self):
        '''If object args are of the correct type'''

        my_model_0 = Place()
        args_dict = {"city_id": "ny123", "user_id": "123", "name": "betty",
                     "description": "test", "number_rooms": "14",
                     "number_bathrooms": "18", "max_guest": "100",
                     "price_by_night": "150", "latitude": "1235.8657",
                     "longitude": "1234.6456",
                     "amenity_ids": "5yycy"}
        usr_dict = my_model_0.to_dict()
        usr_dict.update(args_dict)
        my_model_0 = Place(**usr_dict)
        usr_dict = my_model_0.to_dict()
        city_id = usr_dict['city_id']
        user_id = usr_dict['user_id']
        name = usr_dict['name']
        description = usr_dict['description']
        number_rooms = usr_dict['number_rooms']
        number_bathrooms = usr_dict['number_bathrooms']
        max_guest = usr_dict['max_guest']
        price_by_night = usr_dict['price_by_night']
        latitude = usr_dict['latitude']
        longitude = usr_dict['longitude']
        amenity_ids = usr_dict['amenity_ids']
        self.assertTrue(type(city_id) == str)
        self.assertTrue(type(user_id) == str)
        self.assertTrue(type(description) == str)
        self.assertTrue(type(name) == str)
        self.assertTrue(type(my_model_0.number_rooms) == int)
        self.assertTrue(type(number_bathrooms) == int)
        self.assertTrue(type(max_guest) == int)
        self.assertTrue(type(price_by_night) == int)
        self.assertTrue(type(latitude) == float)
        self.assertTrue(type(longitude) == float)
        self.assertTrue(type(amenity_ids) == list)