from .IHidServer import *

ServiceList = [
    [0x0, '0', 'CreateAppletResource', 'hid::IHidServer'], # 0, 1, 2, 3
    [0x1, '1', 'ActivateDebugPad', 'hid::IHidServer'],
    [],
    [],
]

def get_servicename_by_hex(hex):
    for i in ServiceList:
        if str(i[0]) == hex:
            return i[0], i[2] # return hex and name
        elif int(hex, 16) == int(i[1]): # if decimal of hex == int form of hex
            return i[0], i[2], i[3] # return hex and name

def get_servicename_by_cmdint(cmd):
    for i in ServiceList:
        if i[1] == str(cmd):
            return i[0], i[2], i[3] # return hex, name and service
