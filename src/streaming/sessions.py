"""
sessions.py
-----------
Implement the ListeningSession class for recording listening events.

Classes to implement:
  - ListeningSession
"""
from streaming.users import User
from streaming.tracks import Track
class ListeningSession:
    def __init__(self,session_id,timestamp,duration_listened_seconds):
        self.session_id = session_id
        self.user = User
        self.track = Track
        self.timestamp = timestamp
        self.duration_listened_seconds = duration_listened_seconds
    def duration_listened_minutes(self):
        return self.duration_listened_seconds // 60