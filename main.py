from fastapi import FastAPI
from routes import users, events, speakers, registrations

app = FastAPI(title="Event Management API")

app.include_router(users.router)
app.include_router(events.router)
app.include_router(speakers.router)
app.include_router(registrations.router)
