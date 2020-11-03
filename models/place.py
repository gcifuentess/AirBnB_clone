#!/usr/bin/env python3
'''Place module '''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Place Class'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        check_args = {}
        if kwargs == {}:
            # entered here through Create command from Console
            self.city_id = Place.city_id
            self.user_id = Place.user_id
            self.name = Place.name
            self.description = Place.description
            self.number_rooms = Place.number_rooms
            self.number_bathrooms = Place.number_bathrooms
            self.max_guest = Place.max_guest
            self.price_by_night = Place.price_by_night
            self.latitude = Place.latitude
            self.longitude = Place.longitude
            self.amenity_ids = Place.amenity_ids
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()
            check_args['number_rooms'] = int(kwargs['number_rooms'])
            check_args['number_bathrooms'] = int(kwargs['number_bathrooms'])
            check_args['max_guest'] = int(kwargs['max_guest'])
            check_args['price_by_night'] = int(kwargs['price_by_night'])
            check_args['latitude'] = float(kwargs['latitude'])
            check_args['longitude'] = float(kwargs['longitude'])
            check_args['amenity_ids'] = list(kwargs['amenity_ids'])

        super(Place, self).__init__(*args, **kwargs)
