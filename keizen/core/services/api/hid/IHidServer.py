import datetime, random, threading
import asyncio, enum, inspect
import os
from ..IpcHandler import * # python bad
from .IHidServerServices import IHidServer_ServiceList

def matcher(num, byte:str):
    if num != 'keizenNoNum':
        num = int(num)
        h = hex(num)
        h = h.upper()
        return h
    elif byte != 'keizenNoByte':
        i = int(str(byte), 16)
        return i

class IHidServer(IpcHandler):

    def __init__(self, id: count, isDomain: bool) -> None:
        super().__init__(id, isDomain)
        pass

    def onReceiveServiceId(num, byte):
        if hex(num) in IHidServer_ServiceList:
            matcher(num=num, byte='KeizenNoByte')
        elif str(byte) in IHidServer_ServiceList:
            matcher(num='keizenNoNum', byte=byte)