from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    name: str
    genres: List[str]


class Track(BaseModel):
    name: str
    author: str


class MusicTasteRequestBody(BaseModel):
    tracks: List[Track]
    authors: List[Author]
