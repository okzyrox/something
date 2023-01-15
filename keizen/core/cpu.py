# cpu.py

import random, inspect
import asyncio
import datetime
import threading
import enum


class CpuErrors(enum.Enum):
    cpuInitFailed = 1
    cpuCreationFailed = 2
    cpuReceiveInvalidDataAbort = 3
    cpuSendInvalidDataAbort = 4
    cpuGenericError = 5

class ExceptionCodes(enum.Enum):
    serviceCall = 0x0b010101
    pcAlignmentFault = 0x0b100010
    dataAbort = 0x0b100100
    insnAbort = 0x0b011000


class CpuCore():
    number:int
    quitting = False
    def __init__(self, number:int):
        self.number = number
        thread = threading.Thread(target=self, args=None)
        thread.run()
    
    def loop():
        def get_reg(reg) -> int:
            val:int = 0
            return val # i dont read
    

    def force_execute(*args):
        print(args)    
    

