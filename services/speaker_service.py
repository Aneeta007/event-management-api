from data.store import speakers

def get_speakers():
    return speakers

def get_speaker(speaker_id):
    return next((s for s in speakers if s["id"] == speaker_id), None)
