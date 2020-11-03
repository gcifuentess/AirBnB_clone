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
            # entered here through Create command from Console
            self.email = User.email
            self.password = User.password
            self.first_name = User.first_name
            self.last_name = User.last_name
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()

        super(User, self).__init__(*args, **check_args)
