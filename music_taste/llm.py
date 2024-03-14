from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM

llm: LLM = G4FLLM(
    model=models.gpt_35_turbo,
    provider=Provider.Koala,
)
