from fastapi import APIRouter, HTTPException
from datetime import datetime
from data.store import registrations, registration_id_seq, users, events
from schemas.registration import Registration, RegistrationCreate

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.post("/", response_model=Registration)
def register_user(reg: RegistrationCreate):
    global registration_id_seq

    # Validations
    if reg.user_id not in users or not users[reg.user_id]["is_active"]:
        raise HTTPException(status_code=400, detail="Invalid or inactive user")
    if reg.event_id not in events or not events[reg.event_id]["is_open"]:
        raise HTTPException(status_code=400, detail="Invalid or closed event")
    for r in registrations.values():
        if r["user_id"] == reg.user_id and r["event_id"] == reg.event_id:
            raise HTTPException(status_code=400, detail="User already registered for this event")

    new_reg = {
        "id": registration_id_seq,
        "user_id": reg.user_id,
        "event_id": reg.event_id,
        "registration_date": datetime.now(),
        "attended": False
    }
    registrations[registration_id_seq] = new_reg
    registration_id_seq += 1
    return new_reg

@router.get("/", response_model=list[Registration])
def all_regs():
    return list(registrations.values())

@router.get("/user/{user_id}", response_model=list[Registration])
def get_user_regs(user_id: int):
    return [r for r in registrations.values() if r["user_id"] == user_id]

@router.patch("/{reg_id}/attend")
def mark_attendance(reg_id: int):
    if reg_id in registrations:
        registrations[reg_id]["attended"] = True
        return {"detail": "Attendance marked"}
    raise HTTPException(status_code=404, detail="Registration not found")
