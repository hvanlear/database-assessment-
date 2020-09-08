"""Forms for playlist app."""

from wtforms import SelectMultipleField, StringField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Name", validators=[
                       InputRequired(), Length(min=1, max=45)])
    description = StringField('Description', validators=[
                              InputRequired(), Length(min=1, max=45)])
    # song = SelectMultipleField('Songs', validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Title', validators=[
        InputRequired(), Length(min=1, max=45)])
    artist = StringField('Artist', validators=[
        InputRequired(), Length(min=1, max=45)])
    genre = SelectField(
        "Song Genre",
        choices=[("rap", "Rap"), ("rock", "Rock"),
                 ("pop", "Pop"), ('country', 'Country')],
    )

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
