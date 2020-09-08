"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):

    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    songs = db.relationship(
        'Song', secondary='playlistsong', backref='playlist')


class Song(db.Model):
    __tablename__ = 'song'
    """Song."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=True)


class PlaylistSong(db.Model):
    __tablename__ = 'playlistsong'

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlist.id'), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
