SYSTEM_MESSAGE = "You're a famous music critic and music lover who has spent a lifetime researching music trends and musical tastes. I'm going to write you a list of tracks and artists that I like. Please, advise me 6 tracks that I will like. Select tracks from bands that are not very popular and don't include tracks from my list. Write tracks as JSON array of strings. Write ONLY tracks names in JSON, without any other words."

EXAMPLES = [
    {"input": """
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
""", "output": "[\"Poncho and Lefty\",\"Coat of Many Colors\",\"Blue Eyes Crying in the Rain\",\"All Too Well\",\"I'm So Lonesome I Could Cry\",\"Jesus, Take the Wheel\"]"},
]
