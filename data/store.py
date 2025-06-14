from datetime import datetime

users = {}
events = {}
speakers = {
    1: {"id": 1, "name": "Mr Rotimi", "topic": "Introduction to Python"},
    2: {"id": 2, "name": "Ms Anita", "topic": "How to get away with Murder"},
    3: {"id": 3, "name": "Mr Temitope", "topic": "How to succeed in Yahoo business"}
}
registrations = {}

user_id_seq = 1
event_id_seq = 1
speaker_id_seq = 4
registration_id_seq = 1
