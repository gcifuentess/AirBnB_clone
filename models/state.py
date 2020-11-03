#!/usr/bin/env python3
'''State module '''
from models.base_model import BaseModel


class State(BaseModel):
    '''State Class'''
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        check_args = {}
        if kwargs == {}:
            # entered here through Create command from Console
            self.name = State.name
        else:
            # entered here through Update command from Console
            check_args = kwargs.copy()

        super(State, self).__init__(*args, **kwargs)
