import json
import re
from langchain.schema.output_parser import BaseLLMOutputParser
from music_suggestions.messages import SYSTEM_MESSAGE, EXAMPLES
from music_suggestions.llm import llm
from shared.create_few_shot_prompt_template import create_few_shot_prompt_template
from langchain_core.messages import AIMessage

music_suggestions_final_prompt = create_few_shot_prompt_template(
    SYSTEM_MESSAGE, EXAMPLES)

JSON_ARRAY_REGEXP = re.compile('\[\s{0,1}\".+\"\s{0,1}\]')


def parseJSONArray(ai_message: str) -> str:
    matching_string = JSON_ARRAY_REGEXP.findall(ai_message)
    if len(matching_string) == 0:
        return []
    else:
        matching_string = matching_string[0]
        return json.loads(matching_string)


music_suggestions_chain = music_suggestions_final_prompt | llm | parseJSONArray
