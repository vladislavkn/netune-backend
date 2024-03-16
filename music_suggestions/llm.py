from langchain_g4f import G4FLLM
from shared.config import config
from g4f import Provider, models
from langchain.llms.base import LLM


llm: LLM = G4FLLM(
    model=models.__dict__[config['SUGGESTIONS_LLM_MODEL']],
    provider=Provider.__dict__[config['SUGGESTIONS_LLM_PROVIDER']],
)
