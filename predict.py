import pickle
import time
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.generate_tts import generate_tts_prompt
from base import llm_generate

def load_model():
    with open('model/fuzzy_match_action_list.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

def generate_tts(instruction, action_lists):
    prompt = PromptTemplate(
        template=generate_tts_prompt,
        input_variables=["instruction", "action_lists"]
    )
    chain = prompt | llm_generate | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction, "action_lists": action_lists})
    return scenario

def predict(loaded_model, instruction):
    predicted_label = loaded_model.predict([instruction])[0]
    recommended_functions = predicted_label.split(',')
    return recommended_functions


def execute_functions(recommended_functions):
    for func in recommended_functions:
        print(f"执行功能：{func}")


def main():
    instruction = "我的女朋友很生气"
    loaded_model = load_model()

    start = time.time()
    recommended_functions = predict(loaded_model, instruction)
    print (f"Human: {instruction}")
    print (f"推荐的功能组合是：{recommended_functions}")
    action_lists_str = ", ".join(recommended_functions)
    fuzzy_reponse = generate_tts(instruction, action_lists_str)
    print (f"语音合成：{fuzzy_reponse}")
    end = time.time()
    print (f"模型推理用时：{end - start} seconds")
    execute_functions(recommended_functions)





if __name__ == '__main__':
    main()








