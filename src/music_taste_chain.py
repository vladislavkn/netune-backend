from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from llm_model import llm

SYSTEM_MESSAGE = "You're a famous music critic and music lover who has spent a lifetime researching music trends and musical tastes. I'm going to write you a list of tracks and artists that I like. Please make a psychological portrait of me and describe which tracks and authors helped you to make such conclusions about me. Communicate respectfully and write a short text with no more than 6 sentences. Don't give anything but the text in your reply."

examples = [
    {
        "input": """
The list of the tracks with authors in the brackets:
- The Hanging Tree (James Newton Howard, Jennifer Lawrence)
- Don't Stay (Linkin Park)
- Праздник последнего дня (Мотогонки)
- A Girl Like You (Edwyn Collins)
- Rosenrot (Rammstein)
- Утро (Дайте танк (!))
- Можно я с тобой (AP$ENT)
- Need You Tonight (INXS)
- You See Big Girl / T:T (Hiroyuki Sawano)
- This Is Home (Cavetown)
- Hatef--k (The Bravery)
- Lonely Day (System Of A Down)

The list of the artists with their genres in brackets:
- Linkin Park ( alternative metal, nu metal, post-grunge, rap metal, rock)
- AP$ENT (belarusian indie)
- Мотогонки
- Дайте танк (!) (russian indie, russian indie rock)
- MAXIMUM THE HORMONE (japanese metalcore)
- David Bowie (art rock, classic rock, glam rock, permanent wave, rock)
- Ногу Свело!
- the bird and the bee (la indie)
- The Bravery (dance-punk, indie rock, modern rock)
- Red Hot Chili Peppers (alternative rock, funk metal, funk rock, permanent wave, rock)
- The Weeknd (canadian contemporary r&b, canadian pop, pop)
- Eisbrecher (neue deutsche harte)
""",
        "output": "Your musical preferences reveal a complex individual with a diverse range of emotions and experiences. The haunting melody of \"The Hanging Tree\" hints at a fascination with darker themes, while the raw energy of Linkin Park's \"Don't Stay\" suggests a propensity for intensity and catharsis. The inclusion of Russian indie rock and Belarusian indie music suggests an appreciation for underground and alternative scenes, while the eclectic mix of genres from artists like MAXIMUM THE HORMONE and David Bowie reflects a willingness to explore different sonic landscapes. Overall, your playlist paints a picture of someone who values authenticity, emotional depth, and a sense of adventure in their musical journey."
    },
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
    {
        "input": """
The list of the tracks with authors in the brackets:
- "Ring of Fire" (Johnny Cash)
- "Jolene" (Dolly Parton)
- "On the Road Again" (Willie Nelson)
- "Love Story" (Taylor Swift)
- "Hey, Good Lookin'" (Hank Williams)
- "Before He Cheats" (Carrie Underwood)
- "Symphony No. 5 in C Minor, Op. 67: I. Allegro con brio" (Beethoven)
- "Eine kleine Nachtmusik, K. 525: I. Allegro" (Mozart)
- "Air on the G String" (Bach)
- "1812 Overture, Op. 49" (Tchaikovsky)
- "Hungarian Dance No. 5 in G Minor" (Brahms)
- "Nocturne in E-flat Major, Op. 9, No. 2" (Chopin)

The list of the artists with their genres in brackets:
- Johnny Cash (Country, Rockabilly)
- Dolly Parton (Country, Bluegrass)
- Willie Nelson (Country, Outlaw country)
- Taylor Swift (Country pop, Pop)
- Hank Williams (Country, Honky-tonk)
- Carrie Underwood (Country pop, Country rock)
- Ludwig van Beethoven (Classical, Romantic)
- Wolfgang Amadeus Mozart (Classical, Classical period)
- Johann Sebastian Bach (Baroque, Classical)
- Pyotr Ilyich Tchaikovsky (Romantic, Russian classical)
- Johannes Brahms (Romantic, German classical)
- Frederic Chopin (Romantic, Polish classical)
""",
        "output": "Your diverse selection of tracks suggests a deep appreciation for both classic country and classical music, indicating a multifaceted personality with a refined taste in art and culture. The inclusion of iconic country hits like \"Jolene\" by Dolly Parton and \"Ring of Fire\" by Johnny Cash highlights a connection to storytelling and emotion, while classical masterpieces such as Beethoven's \"Symphony No. 5\" and Chopin's \"Nocturne in E-flat Major\" reveal a penchant for timeless beauty and complexity. Your playlist showcases a harmonious blend of genres, reflecting a soul that finds solace in both the heartfelt lyrics of country ballads and the transcendent melodies of classical compositions."
    }
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
