import datetime, random, threading
import asyncio, enum, inspect
import os
from ..IpcHandler import * # python bad
from .IHidServerServices import *

def matcher(num, hex:str, get):
    if get == 'corresponding':
        if num != 'keizenNoNum':
            num = int(num)
            h = hex(num)
            h = h.upper()
            return h
        elif hex != 'keizenNoByte':
            i = int(str(hex), 16)
            return i
    elif get == 'func':
        if num != 'keizenNoNum':
            i = get_servicename_by_cmdint(1)
            return i[2]
        elif hex != 'keizenNoByte':
            x = get_servicename_by_hex(hex)
            return x[2]
            

class IHidServer(IpcHandler):

    def __init__(self, id: count, isDomain: bool) -> None:
        super().__init__(id, isDomain)
        #pass

    def onReceiveServiceIdReturnFunc(num):
        x = get_servicename_by_cmdint(1)

        cmdnum = x[0]
        funcname = x[1]
        service = x[2]

        print(cmdnum, funcname, service)

        matcher(num=cmdnum, hex='KeizenNoByte', get='func')
    
    def onReceiveServiceHexReturnFunc(hex):
        x = get_servicename_by_hex(hex)

        cmdhex = x[0]
        funcname = x[1]
        service = x[2]

        print(cmdhex, funcname, service)

        matcher(num='KeizenNoNum', hex=cmdhex, get='func')
