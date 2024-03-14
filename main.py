from fastapi import FastAPI

from music_taste.chain import music_taste_chain
from music_suggestions.chain import music_suggestions_chain
from shared.format_info_prompt import format_info_prompt
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
    prompt = format_info_prompt(data.tracks, data.authors)
    return music_taste_chain.invoke({"input": prompt})


@app.post('/suggestions')
def taste(data: MusicTasteRequestBody):
    prompt = format_info_prompt(data.tracks, data.authors)
    return music_suggestions_chain.invoke({"input": prompt})
