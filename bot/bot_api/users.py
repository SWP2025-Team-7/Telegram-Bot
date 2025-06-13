import logging
import requests as re

def register_user():
    re.post("http://127.0.0.1:8000/users/register")