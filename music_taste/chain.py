from .messages import SYSTEM_MESSAGE, EXAMPLES
from .llm import llm
from shared.create_few_shot_prompt_template import create_few_shot_prompt_template

music_taste_final_prompt = create_few_shot_prompt_template(
    SYSTEM_MESSAGE, EXAMPLES)

music_taste_chain = music_taste_final_prompt | llm
