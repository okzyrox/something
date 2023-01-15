from . import *

def main():
    print("Running...")
    handler.loop(
        "nn::hid::IHidServer::GetGyroscopeZeroDriftMode", 
        "nn::hid::IHidServer::SetGyroscopeZeroDriftMode",
        "nn::hid::IHidDebugServer::GetTouchScreenConfiguration"
        )

def test():
    print("Testing...")
    logger.logging.debug("Test")
