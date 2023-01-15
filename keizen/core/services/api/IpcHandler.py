import datetime, random, threading
import asyncio, enum, inspect
import os

count = 1

class IpcHandler():
    def __init__(self, id:count, isDomain:bool) -> None:
        IpcHandler = self
        self.id:int
        count+=1
        self.isDomain = isDomain

    def IpcHandler(server=None):
        if server is not None:
            pass