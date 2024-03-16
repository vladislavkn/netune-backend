from shared.config import config
from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM

llm: LLM = G4FLLM(
    model=models.__dict__[config['TASTE_LLM_MODEL']],
    provider=Provider.__dict__[config['TASTE_LLM_PROVIDER']],
)
