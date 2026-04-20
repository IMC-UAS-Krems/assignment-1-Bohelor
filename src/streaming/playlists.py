"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""
from streaming.users import User
class Playlist:
    def __init__(self,playlist_id,title,owner=None,tracks=None):
        self.playlist_id = playlist_id
        self.title = title
        self.owner = owner
        self.tracks = tracks if tracks is not None else []
    def add_track(self, track):
        if all(getattr(t,"track_id",None) != getattr(track,"track_id",None) for t in self.tracks):
            self.tracks.append(track)
    def remove_track(self, track):
        if isinstance(track, str):
            self.tracks = [t for t in self.tracks if getattr(t, 'track_id', None) != track]
        else:
            self.tracks.remove(track)
    def total_duration_seconds(self):
        return sum(getattr(track,"duration_seconds",0) for track in self.tracks)
class CollaborativePlaylist(Playlist):
    def __init__(self,playlist_id,title,owner=None):
        super().__init__(playlist_id,title,owner)
        self.contributors = [owner] #always include owner as a contributor
    def add_contributor(self, contributor):
        if contributor not in self.contributors:
            self.contributors.append(contributor)
    def remove_contributor(self, contributor):
        if contributor == self.owner:
            raise ValueError("Cannot remove the owner from contributors")
        if contributor in self.contributors:
            self.contributors.remove(contributor)
    def __str__(self):
        contributor_list = ", ".join([str(c) for c in self.contributors])
        track_list = "\n".join(f"  {t.title} by {t.artist}" for t in self.tracks)
        return f"Collaborative Playlist: {self.title}\nContributors: {contributor_list}\nTracks:\n{track_list}"


