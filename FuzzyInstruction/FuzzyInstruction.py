from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from base import llm

from prompts.prompts import *

def fuzzy_scene_generate_actual_scene(instruction):
    prompt = PromptTemplate(
        template=fuzzy_instruction_prompt,
        input_variables=["query"]
    )
    chain = prompt | llm | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction})
    return scenario