from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, BertForSequenceClassification, BertTokenizerFast, BertTokenizer, BertModel, pipeline
import torch
import time

model_path = "/home/ubuntu/iScenario/LLM_Assist/model"

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


start = time.time()
print(nlp("打开左车窗")[0])
end1 = time.time()
print(f"Execution time: {end1 - start} seconds")

# print(nlp("请你帮我关后备箱"))
# end2 = time.time()
# print(f"Execution time: {end2 - start} seconds")

# print(nlp("帮我开左窗户"))

