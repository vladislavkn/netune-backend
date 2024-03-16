
import os
from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM

llm: LLM = G4FLLM(
    model=models.__dict__[os.environ.get('TASTE_LLM_MODEL', 'gpt_35_turbo')],
    provider=Provider.__dict__[os.environ.get(
        'TASTE_LLM_PROVIDER', 'FlowGpt')],
)
