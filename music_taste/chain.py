from .messages import SYSTEM_MESSAGE, EXAMPLES
from .llm import llm
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=EXAMPLES,
)

music_taste_final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_MESSAGE),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

music_taste_chain = music_taste_final_prompt | llm
