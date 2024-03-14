from pydantic import BaseModel


class Author(BaseModel):
    name: str
    genres: list[str]


class Track(BaseModel):
    name: str
    authors: list[str]


class MusicTasteRequestBody(BaseModel):
    tracks: list[Track]
    authors: list[Author]
