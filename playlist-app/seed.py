from models import Playlist, PlaylistSong, Song, db

from app import app

db.drop_all()
db.create_all()

songs = [Song(title='song1', artist='artist1', genre='Rap'),
         Song(title='song2', artist='artist1', genre='Country'),
         Song(title='song3', artist='artist2', genre='Rock')]


playlists = [
    Playlist(
        name='Playlist One', description='A Playlist with a number of songs'),
    Playlist(
        name='Playlist Two', description='Another Playlist with a number of songs')
]

playlistsongs = [
    PlaylistSong(song_id=1, playlist_id=1),
    PlaylistSong(song_id=2, playlist_id=1),
    PlaylistSong(song_id=3, playlist_id=1),
    PlaylistSong(song_id=1, playlist_id=2),
    PlaylistSong(song_id=2, playlist_id=2),
    PlaylistSong(song_id=3, playlist_id=2)
]


db.session.add_all(songs)
db.session.commit()

db.session.add_all(playlists)
db.session.commit()

db.session.add_all(playlistsongs)
db.session.commit()
