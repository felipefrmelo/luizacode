from fastapi import FastAPI

from src.server.database import connect_db, disconnect_db


from src.routers import address, users


app = FastAPI()

app.include_router(address.router)
app.include_router(users.router)

app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", disconnect_db)

