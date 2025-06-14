import logging
import json
import requests as re

def register_user(user_id, alias):
    logging.info(f"Registring user ID:{user_id}, Alias:{alias}")
    try :
        data = {
            "userId": user_id,
            "alias": alias
        }
        ans = re.get("http://127.0.0.1:8000/users/register", data=json.dumps(data), headers={'Content-Type': 'application/json'})
    except Exception as e:
        logging.error(f"Connection Error while trying to register user ID:{user_id}, Alias:{alias}")
    