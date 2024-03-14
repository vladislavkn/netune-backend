from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)


def create_few_shot_prompt_template(system_message: str, examples: list) -> ChatPromptTemplate:
    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{output}"),
        ]
    )

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
    )

    return ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )
