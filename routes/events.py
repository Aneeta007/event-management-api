from fastapi import APIRouter, HTTPException
from schemas.event import Event, EventCreate
from data.store import events, event_id_seq

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=Event)
def create_event(event: EventCreate):
    global event_id_seq
    new_event = event.dict()
    new_event["id"] = event_id_seq
    events[event_id_seq] = new_event
    event_id_seq += 1
    return new_event

@router.get("/", response_model=list[Event])
def get_events():
    return list(events.values())

@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, event: EventCreate):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    events[event_id].update(event.dict())
    return events[event_id]

@router.delete("/{event_id}")
def delete_event(event_id: int):
    if event_id in events:
        del events[event_id]
        return {"detail": "Event deleted"}
    raise HTTPException(status_code=404, detail="Event not found")

@router.patch("/{event_id}/close")
def close_event(event_id: int):
    if event_id in events:
        events[event_id]["is_open"] = False
        return {"detail": "Event closed"}
    raise HTTPException(status_code=404, detail="Event not found")
