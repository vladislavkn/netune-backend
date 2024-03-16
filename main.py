import logging
from fastapi.middleware.cors import CORSMiddleware
from shared.config import config
from shared.models import MusicTasteRequestBody
from shared.format_info_prompt import format_info_prompt
from music_suggestions.chain import music_suggestions_chain
from music_taste.chain import music_taste_chain
from fastapi import FastAPI


app = FastAPI()
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.__dict__[config['LOGLEVEL']],
    format='%(asctime)s %(message)s')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config['FRONTEND_URL']],
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
