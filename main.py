from fastapi import FastAPI

from music_taste.chain import invoke_music_taste_chain
from shared.models import MusicTasteRequestBody
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post('/taste')
def taste(data: MusicTasteRequestBody):
    return invoke_music_taste_chain(data.tracks, data.authors)
