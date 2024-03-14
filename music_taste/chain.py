from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

from .examples import examples
from .llm import llm
from shared.models import Track, Author

SYSTEM_MESSAGE = "You're a famous music critic and music lover who has spent a lifetime researching music trends and musical tastes. I'm going to write you a list of tracks and artists that I like. Please make a psychological portrait of me and describe which tracks and authors helped you to make such conclusions about me. Communicate respectfully and write a short text with no more than 6 sentences. Don't give anything but the text in your reply."


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

music_taste_final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_MESSAGE),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

music_taste_chain = music_taste_final_prompt | llm


def invoke_music_taste_chain(tracks: list[Track], authors: list[Author]) -> str:
    tracks_list = "\n".join(
        map(lambda track: f"- {track.name} ({', '.join(track.authors)})", tracks))
    authors_list = "\n".join(
        map(lambda author: f"- {author.name} ({', '.join(author.genres)})", authors))

    input = f"The list of the tracks with authors in the brackets:\n{tracks_list}\n" + \
        f"The list of the artists with their genres in brackets:\n{authors_list}"

    output = music_taste_chain.invoke({"input": input})
    return output
