from fastapi import FastAPI

import music_taste_chain
from music_types import MusicTasteRequestBody

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post('/taste')
def taste(data: MusicTasteRequestBody):
    input = f"""
The list of the tracks with authors in the brackets:
{map(lambda track: f"- {track.name} ({track.author})\n", data.tracks)}\n
The list of the artists with their genres in brackets:
{map(lambda author: f"- {author.name} ({', '.join(author.genres)})\n", data.authors)}
"""
    return music_taste_chain.invoke({"input": input})