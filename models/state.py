#!/usr/bin/env python3
'''State module '''
from models.base_model import BaseModel


class State(BaseModel):
    '''State Class'''
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super(State, self).__init__(*args, **kwargs)
