from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd

import time


def load_dataset():
    datasets = "/home/ubuntu/iScenario/LLM_Assist/datasets/RZ_FuzzInstruction.csv"

    df = pd.read_csv(datasets)
    return df

def calculate_cosine_similarity(text1, text2):
    vectorize = CountVectorizer()
    vectors = vectorize.fit_transform([text1, text2])

    similarity_score = cosine_similarity(vectors)[0][1]
    return similarity_score

# Method1: sklearn
def method1(instruction, df):
    response, action = "", ""
    for index, row in df.iterrows():
        temp = 0
        user_instruction = row['用户说话']
        score = calculate_cosine_similarity(instruction, user_instruction)
        print (score)
        if score > temp:
            response = row['车辆反馈']
            action = row['动作序列']
            score = temp

    return response, action

def main():
    instruction = "我累了"
    df = load_dataset()
    start1 = time.time()
    response, action = method1(instruction, df)
    print(f"Response: {response}, Action: {action}")
    end1 = time.time()
    print (f"Method1: Execution Time {end1 - start1}")
    

if __name__ == "__main__":
    main()