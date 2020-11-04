#!/usr/bin/env python3
'''City module'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City Class'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super(City, self).__init__(*args, **kwargs)
