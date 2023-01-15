from . import *

def main():
    print("Running...")

def test():
    print("Testing...")
    logger.logging.debug("Test")
    handler.loop(
        "nn::hid::IHidServer::GetGyroscopeZeroDriftMode", 
        "nn::hid::IHidServer::SetGyroscopeZeroDriftMode",
        "nn::hid::IHidDebugServer::GetTouchScreenConfiguration"
        )
    ihid = IHidServer
    print(ihid.onReceiveServiceIdReturnFunc(1))
    print(ihid.onReceiveServiceHexReturnFunc('0x0'))
