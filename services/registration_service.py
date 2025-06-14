from datetime import datetime
from data.store import registrations, registration_id_seq, users, events

def create_registration(user_id: int, event_id: int):
    global registration_id_seq

    user = next((u for u in users if u["id"] == user_id and u["is_active"]), None)
    if not user:
        return {"error": "User is inactive or does not exist"}

    event = next((e for e in events if e["id"] == event_id and e["is_open"]), None)
    if not event:
        return {"error": "Event is closed"}

    already_registered = any(r for r in registrations if r["user_id"] == user_id and r["event_id"] == event_id)
    if already_registered:
        return {"error": "User already registered for this event"}

    reg = {
        "id": registration_id_seq,
        "user_id": user_id,
        "event_id": event_id,
        "registration_date": datetime.now(),
        "attended": False
    }

    registrations.append(reg)
    registration_id_seq += 1
    return reg

def mark_attendance(registration_id):
    reg = next((r for r in registrations if r["id"] == registration_id), None)
    if reg:
        reg["attended"] = True
    return reg

def get_registrations():
    return registrations

def get_user_registrations(user_id):
    return [r for r in registrations if r["user_id"] == user_id]

def get_attendees():
    return [r for r in registrations if r["attended"]]
