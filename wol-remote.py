import os
import wollib
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

load_dotenv()
app = FastAPI()

def _handle():
    raw_addresses = os.getenv("MAC_ADDRESSES")
    if not raw_addresses:
        raise Exception("MAC_ADDRESSES env variable not set")
    mac_list = [mac.strip() for mac in raw_addresses.split(",") if mac.strip()]
    for mac in mac_list:
        wollib.wake(mac)

@app.get("/api/wake")
async def wake_endpoint():
    try:
        _handle()
        return {"status": "sent" }
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get("/", response_class=HTMLResponse)
async def web():
    return HTMLResponse(content=open("index.html").read())

if __name__ == "__main__":
    _handle()