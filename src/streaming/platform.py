from datetime import datetime, timedelta
from streaming.tracks import Song
from streaming.playlists import CollaborativePlaylist

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

    def all_sessions(self):
        return list(self.sessions)


    # Q1
    def total_listening_time_minutes(self, start: datetime, end: datetime):
        total_seconds = 0
        for session in self.sessions:
            if start <= session.timestamp <= end:
                total_seconds += session.duration_listened_seconds
        return total_seconds / 60


    # Q2
    def avg_unique_tracks_per_premium_user(self, days=30):
        cutoff = datetime.now() - timedelta(days=days)
        premium_users = [u for u in self.users if u.subscription_type == "Premium"]
        if not premium_users:
            return 0.0
        counts = []
        for user in premium_users:
            track_ids = set()
            for session in self.sessions:
                if session.user.user_id != user.user_id:
                    continue
                if session.timestamp < cutoff:
                    continue
                track_ids.add(session.track.track_id)
            counts.append(len(track_ids))
        return sum(counts) / len(counts)


    # Q3
    def track_with_most_distinct_listeners(self):
        listeners = {}
        for session in self.sessions:
            track = session.track
            user_id = session.user.user_id
            if track not in listeners:
                listeners[track] = set()
            listeners[track].add(user_id)
        if not listeners:
            return None
        return max(listeners, key=lambda t: len(listeners[t]))


    # Q4
    def avg_session_duration_by_user_type(self):
        types = ["FreeUser", "PremiumUser", "FamilyAccountUser", "FamilyMember"]
        durations = {t: [] for t in types}
        for session in self.sessions:
            user_type = type(session.user).__name__
            if user_type in durations:
                durations[user_type].append(session.duration_listened_seconds)
        result = []
        for t in types:
            if durations[t]:
                avg = sum(durations[t]) / len(durations[t])
            else:
                avg = 0.0
            result.append((t, avg))
        return sorted(result, key=lambda x: x[1], reverse=True)


    # Q5
    def total_listening_time_underage_sub_users_minutes(self, age_threshold=18):
        total_seconds = 0
        for session in self.sessions:
            user = session.user
            if type(user).__name__ == "FamilyMember" and user.age < age_threshold:
                total_seconds += session.duration_listened_seconds
        return total_seconds / 60


    # Q6
    def top_artists_by_listening_time(self, n=5):
        artist_time = {}
        for session in self.sessions:
            track = session.track
            if isinstance(track, Song):
                artist = track.artist
                artist_time[artist] = artist_time.get(artist, 0) + session.duration_listened_seconds
        sorted_artists = sorted(
            artist_time.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return [(artist, seconds / 60) for artist, seconds in sorted_artists[:n]]


    # Q7
    def user_top_genre(self, user_id):
        genre_time = {}
        total = 0
        for session in self.sessions:
            if session.user.user_id != user_id:
                continue
            genre = session.track.genre
            duration = session.duration_listened_seconds
            genre_time[genre] = genre_time.get(genre, 0) + duration
            total += duration
        if total == 0:
            return None
        top_genre = max(genre_time, key=genre_time.get)
        percentage = (genre_time[top_genre] / total) * 100
        return top_genre, percentage


    # Q8
    def collaborative_playlists_with_many_artists(self, threshold=3):
        result = []
        for playlist in self.playlists:
            if not isinstance(playlist, CollaborativePlaylist):
                continue
            artists = set()
            for track in playlist.tracks:
                if isinstance(track, Song):
                    artists.add(track.artist)
            if len(artists) > threshold:
                result.append(playlist)
        return result


    # Q9
    def avg_tracks_per_playlist_type(self):
        counts = {"Playlist": 0, "CollaborativePlaylist": 0}
        totals = {"Playlist": 0, "CollaborativePlaylist": 0}
        for playlist in self.playlists:
            if isinstance(playlist, CollaborativePlaylist):
                key = "CollaborativePlaylist"
            else:
                key = "Playlist"
            counts[key] += 1
            totals[key] += len(playlist.tracks)
        return {
            key: (totals[key] / counts[key] if counts[key] > 0 else 0.0)
            for key in counts
        }
    

    # Q10
    def users_who_completed_albums(self):
        result = []
        for user in self.users:
            listened = set()
            for session in self.sessions:
                if session.user.user_id == user.user_id:
                    listened.add(session.track.track_id)
            completed = []
            for album in self.albums:
                album_ids = {track.track_id for track in album.tracks}
                if album_ids and album_ids.issubset(listened):
                    completed.append(album.title)
            if completed:
                result.append((user, completed))
        return result