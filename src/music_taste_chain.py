from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from src.llm_model import llm
from src.music_types import Track, Author

SYSTEM_MESSAGE = "You're a famous music critic and music lover who has spent a lifetime researching music trends and musical tastes. I'm going to write you a list of tracks and artists that I like. Please make a psychological portrait of me and describe which tracks and authors helped you to make such conclusions about me. Communicate respectfully and write a short text with no more than 6 sentences. Don't give anything but the text in your reply."

examples = [
    {"input": """
The list of the tracks with authors in the brackets:
- he Thrill Is Gone (B.B. King)
- Gin and Juice (Snoop Dogg)
- Crossroads (Bone Thugs-N-Harmony)
- Lose Yourself (Eminem)
- Boom Boom (John Lee Hooker)
- Empire State of Mind (Jay-Z ft. Alicia Keys)
- I'm Your Hoochie Coochie Man (Muddy Waters)
- Ms. Jackson (OutKast)
- Black Betty (Lead Belly)
- Nuthin' but a 'G' Thang (Dr. Dre ft. Snoop Dogg)
- Sinnerman (Nina Simone)
- Juicy (The Notorious B.I.G.)

The list of the artists with their genres in brackets:
- B.B. King (Blues, R&B)
- Snoop Dogg (Hip-hop, G-funk)
- Bone Thugs-N-Harmony (Hip-hop, R&B, Midwest hip-hop)
- Eminem (Hip-hop, Rap rock)
- John Lee Hooker (Blues, Boogie-woogie)
- Jay-Z (Hip-hop, East Coast hip-hop)
- Muddy Waters (Blues, Chicago blues)
- OutKast (Hip-hop, Southern hip-hop, Funk)
- Lead Belly (Blues, Folk)
- Dr. Dre (Hip-hop, G-funk)
- Nina Simone (Jazz, Blues, Soul)
- The Notorious B.I.G. (Hip-hop, East Coast hip-hop)
""", "output": "Your playlist reflects a deep appreciation for the roots of hip-hop and the blues, suggesting a connection to raw emotion and authenticity in music. Tracks like \"The Thrill Is Gone\" by B.B. King and \"I'm Your Hoochie Coochie Man\" by Muddy Waters reveal a reverence for classic blues, while iconic hip-hop anthems like \"Gin and Juice\" by Snoop Dogg and \"Lose Yourself\" by Eminem showcase a love for storytelling and rhythm. The inclusion of artists like Nina Simone and Lead Belly adds depth, suggesting a desire to explore the rich history and cultural significance of music. Overall, your playlist speaks to a soulful individual who finds solace and inspiration in the timeless sounds of the blues and the expressive narratives of hip-hop."},
]


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
