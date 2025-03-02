#!/usr/bin/python3
import re
import json
from .base_model import BaseModel


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, email))

def validate_password(password):
    pattern = r"[!@#$%^&*()_+\-=\[\]{}|;:'\",.<>?/`~]"
    return bool(re.search(pattern, password))

class User(BaseModel):
    """User Class inherited BaseModel"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.password = password
        self.is_admin = is_admin                                                                                                                          

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Wrong Email Type !")
        if not validate_email(email):
            raise ValueError("Not correct format !")
        else:
            self.__email = email

    # @property
    # def password(self):
    #     return self.__password

    # @password.setter
    # def password(self, password):
    #     if len(password) < 8:
    #         raise ValueError("Password must be > at 8")
            
    #     if not validate_password(password):
    #         raise ValueError("Password must be minimum 1 special caracters")
            
    #     self.__password = password

    def to_dict(self):
        return {
            'id': self.id, 
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'email': self.email
        }
