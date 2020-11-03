#!/usr/bin/env python3
'''City module'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City Class'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        check_args = {}
        if kwargs == {}:
            # entered here through Create command from Console
            self.state_id = City.state_id
            self.name = City.name
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()

        super(City, self).__init__(*args, **kwargs)
