from requests import Session
from uuid import uuid4
from time import time

class IgUtils:
    @staticmethod
    def __xmid__() -> str:
        "get a valid xmid cookie"
        try:
            return (
                Session()
                .get(
                    "https://www.instagram.com/web/__mid/",
                )
                .text
            )
        except:
            return None

    @staticmethod
    def __csrf__() -> str:
        "get a valid csrftoken cookie"
        try:
            return (
                Session()
                .get(
                    "https://www.instagram.com/data/shared_data/",
                )
                .json()["config"]["csrf_token"]
            )
        except:
            return None

    @staticmethod
    def __deviceid__() -> str:
        "get a valid device_id"
        try:
            return (
                Session()
                .get("https://www.instagram.com/data/shared_data/")
                .json()["device_id"]
            )
        except:
            return None

    @staticmethod
    def __sessionid__() -> str:
        "experimental"
        try:
            return (
                Session()
                .get("https://www.instagram.com/data/shared_data/")
                .cookies["sessionid"]
            )
        except:
            return None

    @staticmethod
    def __get__headers__() -> str:
        try:
            return (
                Session().get("https://www.instagram.com/data/shared_data/").headers
            )
        except:
            return None
    
    @staticmethod
    def __userid__(username: str) -> str:
        "get targets userid"
        try:
            return Session().get("https://storiesig.info/api/ig/userInfoByUsername/{}".format(username)).json()['result']['user']['pk']
        except:
            return None
    
    @staticmethod
    def doUUID4() -> str:
        return ''.join(str(uuid4()))
    
    @staticmethod
    def __enc_pw__(password :str) -> str:
        return f'#PWD:0:{int(time())}:{str(password)}'

# made by @Fhivo on Telegram.