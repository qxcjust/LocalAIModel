from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

text1 = "我累了"
text2 = "我累了"

vectorize = CountVectorizer()
vectors = vectorize.fit_transform([text1, text2])

similarity_score = cosine_similarity(vectors)[0][1]
print (similarity_score)

