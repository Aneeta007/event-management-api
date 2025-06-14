from data.store import events, event_id_counter
from schemas.event import EventCreate, Event

def create_event(event_data: EventCreate) -> Event:
    global event_id_counter
    event = Event(id=event_id_counter, **event_data.dict())
    events[event_id_counter] = event
    event_id_counter += 1
    return event

def get_event(event_id: int) -> Event:
    return events.get(event_id)

def list_events() -> list[Event]:
    return list(events.values())

def update_event(event_id: int, event_data: EventCreate) -> Event:
    if event_id in events:
        updated_event = Event(id=event_id, **event_data.dict())
        events[event_id] = updated_event
        return updated_event
    return None

def delete_event(event_id: int) -> bool:
    return events.pop(event_id, None) is not None
