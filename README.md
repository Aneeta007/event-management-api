Event Management API
Welcome to the Event Management API – a simple backend app built with FastAPI that allows users to register for events, track attendance, and manage both events and speaker details.

This project was created as part of my ALTSchool 2nd Semester Exam and is built entirely with in-memory storage. 

Features
Create and manage users

Create and manage events

Register users for events 

Mark attendance

View all registrations or filter by user

View list of speakers

How to Run
Clone this repo

Install dependencies

Run the server
uvicorn main:app --reload

Check Swagger UI
http://127.0.0.1:8000/docs

Tech Stack
Python 

FastAPI 

Pydantic (for data validation)