from wollib import wake
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    mac_list = [mac.strip() for mac in os.getenv("MAC_ADDRESSES").split(",") if mac.strip()]
    for mac in mac_list:
        wake(mac)