"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
    - Track (abstract base class)
    - Song
    - SingleRelease
    - AlbumTrack
    - Podcast
    - InterviewEpisode
    - NarrativeEpisode
    - AudiobookTrack
"""




class Track:
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str):
        self.track_id = track_id
        self.title = title
        duration_seconds = duration_seconds if duration_seconds >= 0 else 0
        self.duration_seconds = duration_seconds
    def duration_minutes(self):
        return self.duration_seconds / 60

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.track_id == other.track_id
        return False
class Song(Track):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, artist: str):
        super().__init__(track_id, title, duration_seconds, genre)
        self.artist = artist
    def get_info(self):
        return f'{self.title} by {self.artist}'
    def get_info(self):
        return f"{self.title} by {self.artist}"

class SingleRelease(Song):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, artist: str, release_date):
        super().__init__(track_id, title, duration_seconds, genre, artist)
        self.release_date = release_date
    def get_info(self):
        return f"{self.title} by {self.artist} (Released: {self.release_date})"

class Podcast(Track):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, host: str, description: str = ""):
        super().__init__(track_id, title, duration_seconds, genre)
        self.host = host
        self.description = description
    def get_info(self):
        return f"{self.title} hosted by {self.host}"

class InterviewEpisode(Podcast):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, host: str, description: str = "", guest: str = ""):
        super().__init__(track_id, title, duration_seconds, genre, host, description)
        self.guest = guest
    def get_info(self):
        return f"{self.title} - Interview with {self.guest}"

class NarrativeEpisode(Podcast):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, host: str, description: str = "", season: int = 1, episode_number: int = 1):
        super().__init__(track_id, title, duration_seconds, genre, host, description)
        self.season = season
        self.episode_number = episode_number
    def get_info(self):
        return f"{self.title} (S{self.season}E{self.episode_number})"

class AudiobookTrack(Track):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, author: str, narrator: str):
        super().__init__(track_id, title, duration_seconds, genre)
        self.author = author
        self.narrator = narrator
    def get_info(self):
        return f"{self.title} by {self.author}, narrated by {self.narrator}"

class AlbumTrack(Song):
    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, artist: str, track_number: int):
        super().__init__(track_id, title, duration_seconds, genre, artist)
        self.track_number = track_number
        self.album = None
    def get_info(self):
        return f"{self.track_number}. {self.title} by {self.artist}"
