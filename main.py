import os
from fastapi.middleware.cors import CORSMiddleware
from shared.logger import logger
from shared.models import MusicTasteRequestBody
from shared.format_info_prompt import format_info_prompt
from music_suggestions.chain import music_suggestions_chain
from music_taste.chain import music_taste_chain
from fastapi import FastAPI


app = FastAPI()

origin = os.environ.get('FRONTEND_URL', "http://localhost:5432")
logger.info('CORS origin: %s', origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post('/taste')
def taste(data: MusicTasteRequestBody):
    logger.info('Taste request: %s', data.dump_formatted())
    prompt = format_info_prompt(data.tracks, data.authors, personal=False)
    logger.debug('Taste prompt: %s', prompt)

    output = music_taste_chain.invoke({"input": prompt})
    logger.info('Taste output: %s', output)
    return output


@app.post('/suggestions')
def taste(data: MusicTasteRequestBody):
    logger.info('Suggestions request: %s', data.dump_formatted())
    prompt = format_info_prompt(data.tracks, data.authors, personal=True)
    logger.debug('Suggestions prompt: %s', prompt)

    output = music_suggestions_chain.invoke({"input": prompt})
    logger.info('Suggestions output: %s', output)
    return output
