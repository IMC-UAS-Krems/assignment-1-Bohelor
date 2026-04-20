"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
class Album:
    def __init__(self, album_id:str, title:str, artist:str, release_year, tracks:list=None, genre=None):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = tracks if tracks is not None else []
        self.genre = genre
    def add_track(self, track):
        try:
            track.album = self
        except Exception:
            pass
        self.tracks.append(track)
        self.tracks.sort(key=lambda t: getattr(t,"track_number",0))
    def __str__(self):
        track_list = "\n".join(f"  {t.track_number}. {t.title} ({t.duration_seconds}s)" for t in self.tracks)
        return f"Album: {self.title} by {self.artist} ({self.release_year})\nTracks:\n{track_list}"
    def track_ids(self):
        return {track.track_id for track in self.tracks}
    def duration_seconds(self):
        return sum(getattr(track,"duration_seconds",0) for track in self.tracks)
class AlbumTrack(Album):
    def __init__(self,track_id,title,duration_seconds,genre,artist,track_number=None):
        self.track_id = track_id
        self.duration_seconds = duration_seconds
        self.genre = genre
        self.track_number = track_number
        self.title = title
        self.artist = artist
        self.album = None
    def __str__(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    