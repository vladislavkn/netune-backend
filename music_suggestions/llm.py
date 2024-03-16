import os
from langchain_g4f import G4FLLM
from g4f import Provider, models
from langchain.llms.base import LLM


llm: LLM = G4FLLM(
    model=models.__dict__[os.environ.get(
        'SUGGESTIONS_LLM_MODEL', 'gpt-35-turbo')],
    provider=Provider.__dict__[os.environ.get(
        'SUGGESTIONS_LLM_PROVIDER',
        'FlowGpt'
    )],
)
