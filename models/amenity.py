#!/usr/bin/env python3
'''Amenity module'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity Class'''
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super(Amenity, self).__init__(*args, **kwargs)
