# calendar_api

A simple calendar API powered by FastAPI.

## Architecture

```
- database
	- build.py
	- database_handler.py
- server
	- method.py
	- server.py
- client
	- client.py
```

## Usage

1. Clone this repo from GitHub
2. Install Python packages: `fastapi` and `uvicorn`
3. Run `python build.py` to create SQLite database (only run for the first time)
4. Run `uvicorn server:app --reload`
5. Run test code in `python client.py`, or try it out in `http://127.0.0.1:8000/docs`