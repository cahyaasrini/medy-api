import json 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def get_vocab(): 
    vocabfile = 'vocab.json'
    with open(vocabfile) as f: 
        file = json.load(f)

    vocab = []
    for key in file.keys():
        vocab += [file[key][str(i)] for i in range(len(file[key]))]

    return vocab 

vocab = get_vocab()
cv = CountVectorizer(binary=True, vocabulary=vocab)


def cosine(a, b): 
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    return cosine_similarity(a, b)


text = ["fever"]

vector = cv.transform(text)
arr_vector = vector.toarray()

print(arr_vector.shape)
print(arr_vector[0,:])
