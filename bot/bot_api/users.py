import logging
import requests as re

def register_user(user_id, alias):
    logging.info(f"Registring user ID:{user_id}, Alias:{alias}")
    try :
        ans = re.post("http://127.0.0.1:8000/users/register")
    except Exception as e:
        logging.error(f"Connection Error while trying to register user ID:{user_id}, Alias:{alias}") 
    