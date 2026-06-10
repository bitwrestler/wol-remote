# wol-remote

A simple FastAPI service to send Wake-on-LAN (WoL) packets to multiple devices via a REST API.

## Features
- **API Endpoint**: Trigger wake packets for all configured devices via a single GET request.
- **Environment Configuration**: Manage device MAC addresses easily using a `.env` file.
- **Auto-Wake**: Automatically send wake packets to all listed devices when the script is started directly.

## Prerequisites
- Python 3.x
- `wollib`
- `fastapi`
- `uvicorn`
- `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd wol-remote
   ```

2. Install dependencies:
   ```bash
   pip install wollib fastapi uvicorn python-dotenv
   ```

3. Create a `.env` file in the root directory:
   ```env
   MAC_ADDRESSES=00:11:22:33:44:55,66:77:88:99:AA:BB
   ```

## Usage

### Running the Server
Start the FastAPI server using `uvicorn`:
```bash
uvicorn wol-remote:app --host 0.0.0.0 --port 8000
```

### API Endpoints
Trigger a wake command for all devices:
`GET /api/wake`

**Example Response:**
```json
{
  "status": "sent"
}
```

## Development
To run the script directly and trigger a wakeup immediately:
```bash
python wol-remote.py
```
