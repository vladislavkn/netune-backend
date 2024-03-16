import json
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

    def dump_formatted(self):
        model_dict = self.model_dump(mode='json')
        return json.dumps(model_dict, indent=4)
