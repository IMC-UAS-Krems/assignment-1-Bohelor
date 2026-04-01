"""
artists.py
----------
Implement the Artist class representing musicians and content creators.

Classes to implement:
  - Artist
"""
from streaming.albums import Album 
class Artist:
    def __init__(self,artist_id:str, name:str, genre:str):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.tracks = []
        self.albums = []
    def add_track(self, track):
        try:
            track.artist = self
        except Exception:
            pass
        self.tracks.append(track)
    def track_count(self):
        return len(self.tracks)
    def add_album(self, album):
        try:
            album.artist = self.name
        except Exception:
            pass
        self.albums.append(album)
    def single_release(self,title,duration,genre=None,release_year=None):
        single = Album(title,self.name,genre=genre,artist=self.name,release_year=release_year,tracks=[])
        self.add_album(single)
        return single
    def __str__(self):
        album_list = "\n".join(f"  {a.title} ({a.release_year})" for a in self.albums)
        return f"Artist: {self.name} (Genre: {self.genre})\nAlbums:\n{album_list}"