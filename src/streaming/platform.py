"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
class StreamingPlatform:
    def __init__(self,name,catalogue=None,artists=None,albums=None,playlists=None,sessions=None,users=None):
        self.name = name
        self.catalogue = catalogue if catalogue is not None else []
        self.artists = artists if artists is not None else []
        self.albums = albums if albums is not None else []
        self.playlists = playlists if playlists is not None else []
        self.sessions = sessions if sessions is not None else []
        self.users = users if users is not None else []
    def add_track(self, track):
        self.catalogue.append(track)
    def add_artist(self, artist):
        self.artists.append(artist)
    def add_album(self, album):
        self.albums.append(album)
    def add_user(self, user):
        self.users.append(user)
    def add_playlist(self, playlist):
        self.playlists.append(playlist)
    def record_session(self, session):
        self.sessions.append(session)
    def get_track(self, track_id):
        for track in self.catalogue:
            if getattr(track,"track_id",None) == track_id:
                return track
        return None
    def get_user(self, user_id):
        for user in self.users:
            if getattr(user,"user_id",None) == user_id:
                return user
        return None
    def get_artist(self, artist_id):
        for artist in self.artists:
            if getattr(artist,"artist_id",None) == artist_id:
                return artist
        return None
    def get_album(self, album_id):
        for album in self.albums:
            if getattr(album,"album_id",None) == album_id:
                return album
        return None
    def all_users(self):
        return list(self.users)