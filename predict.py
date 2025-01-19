import pickle
import time
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.generate_tts import generate_tts_prompt
from base import llm_tts_generate, llm_generate
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def calculate_similarity(target_text, text_list):
    vectorizer = TfidfVectorizer()
    all_texts = text_list + [target_text]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    target_vector = tfidf_matrix[-1]
    similarities = cosine_similarity(tfidf_matrix[:-1], target_vector)
    max_similarity_index = np.argmax(similarities)
    max_similarity = similarities[max_similarity_index][0]
    return max_similarity_index, max_similarity

def find_max_similarity(csv_file, target_text, text_column, target_column, num_threads=4):
    df = pd.read_csv(csv_file)
    text_list = df[text_column].tolist()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future = executor.submit(calculate_similarity, target_text, text_list)
        max_similarity_index, max_similarity = future.result()
    
    max_similarity_element = df.iloc[max_similarity_index][target_column]
    return max_similarity_element


def load_model():
    with open('model/fuzzy_match_action_list.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

def generate_tts(instruction, action_lists, recommended_response):
    prompt = PromptTemplate(
        template=generate_tts_prompt,
        input_variables=["instruction", "action_lists", "recommended_response"]
    )
    chain = prompt | llm_generate | StrOutputParser()
    scenario = chain.invoke({"instruction": instruction, "action_lists": action_lists, "recommended_response": recommended_response})
    return scenario

def predict(loaded_model, instruction):
    predicted_label = loaded_model.predict([instruction])[0]
    recommended_functions = predicted_label.split(',')
    return recommended_functions


def execute_functions(recommended_functions):
    for func in recommended_functions:
        print(f"执行功能：{func}")


def main():
    instruction = "我可以和外面的人说话吗？"

    csv_file = "/home/ubuntu/iScenario/LLM_Assist/datasets/RZ_FuzzInstruction.csv"
    column_name = "用户说话"
    target_column = "车辆反馈"
    # 矫正权重
    loaded_model = load_model()
    test_functions = predict(loaded_model, "天气很热啊")
    
    start = time.time()
    recommended_functions = predict(loaded_model, instruction)
    start4 = time.time()
    recommended_response = find_max_similarity(csv_file, instruction, column_name, target_column)
    end4 = time.time()
    print (f"计算相似度用时：{end4 - start4} seconds")

    print (f"推荐返回对话: {recommended_response}")
    print (f"Human: {instruction}")
    print (f"推荐的功能组合是：{recommended_functions}")
    action_lists_str = ", ".join(recommended_functions)
    fuzzy_reponse = generate_tts(instruction, action_lists_str, recommended_response)
    print (f"语音合成：{fuzzy_reponse}")
    end = time.time()
    print (f"模型推理用时：{end - start} seconds")
    execute_functions(recommended_functions)





if __name__ == '__main__':
    main()








