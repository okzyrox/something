import datetime, random, threading
import asyncio, enum, inspect
import os
from ..logging import *
from .api import *

class Handler():
    def __init__(self) -> None:
        pass
    

    def locate(*serviceName):
        # ex: nn:hid:GetXpadIds == /api/hid/IHidServer.GetXpadIds
        tem = serviceName[1]
        tem = str(tem)

        x = tem.split("::")
        if len(x) == 4:
            return f"{x[1]}.{x[2]}.{x[3]}"
    
    def loop(self, *args:list):
        for argument in args:
            x = self.locate(argument)
            logging.info(f"Service - {argument} ({x})")
            #api.
            

handler = Handler()