from . import *

def main():
    # Setup config folders and ROM folders, etc
    # Load ROM
    print("Running...")
    handler.loop(
        "nn::hid::IHidServer::GetGyroscopeZeroDriftMode", 
        "nn::hid::IHidServer::SetGyroscopeZeroDriftMode",
        "nn::hid::IHidDebugServer::GetTouchScreenConfiguration"
        )

def test():
    print("Testing...")
    logger.logging.debug("Test")