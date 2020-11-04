#!/usr/bin/env python3
'''User Module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User Class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        check_args = {}
        if kwargs == {}:
            pass
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()
        super(User, self).__init__(*args, **check_args)
