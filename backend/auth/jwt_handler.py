import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JSWT_ALGORITHM = config("algorithm")

def token_response(token: str):
    return {
        "access token": token
    }

def signJWT(userID : str):
    paylod = {
        "userID": userID,
        "expiry": time.time()+600
    }
    token = jwt.encode(paylod, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return  token_response(token)


def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JSWT_ALGORITHM)
        return decode_token if decode_token['expiries']>=time.time() else None
    except:
        return {}