#!/usr/bin/env python3
'''review module'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review Class'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        check_args = {}
        if kwargs == {}:
            # entered here through Create command from Console
            self.place_id = City.place_id
            self.user_id = City.user_id
            self.text = City.text
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()

        super(Review, self).__init__(*args, **kwargs)
