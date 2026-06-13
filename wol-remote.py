import os
import wollib
import time
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

WOL_FILE = "/tmp/wol.dat"
COOLDOWN_SECONDS = 60

load_dotenv()
app = FastAPI()

def _handle():
    raw_addresses = os.getenv("MAC_ADDRESSES")
    if not raw_addresses:
        raise Exception("MAC_ADDRESSES env variable not set")
    mac_list = [mac.strip() for mac in raw_addresses.split(",") if mac.strip()]
    for mac in mac_list:
        wollib.wake(mac)

@app.api_route("/api/wake", methods=["GET", "POST"])
async def wake_endpoint():
    try:
        # Check if we should skip based on the last modified time of WOL_FILE
        if os.path.exists(WOL_FILE):
            mtime = os.path.getmtime(WOL_FILE)
            if (time.time() - mtime) < COOLDOWN_SECONDS:
                return {"status": "skipped"}

        _handle()
        # Update the last modified time of WOL_FILE
        with open(WOL_FILE, "a"):
            os.utime(WOL_FILE, None)
        return {"status": "sent" }
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get("/", response_class=HTMLResponse)
async def web():
    return HTMLResponse(content=open("index.html").read())

if __name__ == "__main__":
    _handle()