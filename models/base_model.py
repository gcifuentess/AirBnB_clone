#!/usr/bin/python3
'''Base Model Module'''
from datetime import datetime
from datetime import date
from uuid import uuid4
import models


class BaseModel:
    ''' Base Model Class '''

    def __init__(self, *args, **kwargs):
        ''' init instances '''
        if ('id' in kwargs.keys() and
                'created_at' in kwargs.keys() and
                'updated_at' in kwargs.keys()):

            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs['id']

                elif key == 'created_at':
                    created = datetime.strptime(kwargs['created_at'],
                                                date_format)
                    self.created_at = created

                elif key == 'updated_at':
                    updated = datetime.strptime(kwargs['updated_at'],
                                                date_format)
                    self.updated_at = updated

                else:
                    if key != '__class__':
                        self.__dict__[key] = value
            models.storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        ''' str representation '''
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        ''' save method to update time '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' to_dict method returns a dict '''
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return(base_dict)
