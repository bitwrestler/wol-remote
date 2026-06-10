import os
import wollib
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI()

def _handle():
    mac_list = [mac.strip() for mac in os.getenv("MAC_ADDRESSES").split(",") if mac.strip()]
    for mac in mac_list:
        wollib.wake(mac)

@app.get("/api/wake")
async def wake_endpoint():
    try:
        _handle()
        return {"status": "sent" }
    except Exception as e:
        raise HTTPException(500, str(e))



if __name__ == "__main__":
    _handle()