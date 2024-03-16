import json
import re
from music_suggestions.messages import SYSTEM_MESSAGE
from music_suggestions.llm import llm
from langchain.prompts import ChatPromptTemplate

music_suggestions_final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_MESSAGE),
        ("human", "{input}"),
    ]
)

JSON_ARRAY_REGEXP = re.compile('\[\s*(\".+\",\s*)*\".+\"\s*\]')


def parseJSONArray(ai_message: str) -> str:
    match = JSON_ARRAY_REGEXP.search(ai_message)
    if match:
        json_array_string = match.group()
        return json.loads(json_array_string)
    else:
        return []


music_suggestions_chain = music_suggestions_final_prompt | llm | parseJSONArray
