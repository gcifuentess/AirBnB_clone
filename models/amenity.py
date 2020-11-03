#!/usr/bin/env python3
'''Amenity module'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity Class'''
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        check_args = {}
        if kwargs == {}:
            # entered here through Create command from Console
            self.name = Amenity.name
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()

        super(Amenity, self).__init__(*args, **kwargs)
