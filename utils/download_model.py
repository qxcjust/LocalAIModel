from transformers import AutoTokenizer, AutoModel

model_name = "Henriquee/bert-text-classification-car-evaluation"

model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

output_folder = "model2"
model.save_pretrained(output_folder)
tokenizer.save_pretrained(output_folder)