from fastapi import FastAPI
from core import Events

import uvicorn



app = FastAPI()

app.add_event_handler("startup", Events.startup(app))
app.add_event_handler("shutdown", Events.stopping(app))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=2345)

