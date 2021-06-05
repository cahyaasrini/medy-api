import json 

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def get_vocab(): 
    vocabfile = 'vocab.json'
    with open(vocabfile) as f: 
        file = json.load(f)

    vocab = []
    for i in range(len(file)):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = alphabet[i]

        obj2 = file[i][key]

        vocab += [ obj2[i]["indication"] for i in range(len(obj2))]

    print(vocab)

    return vocab 

# def cosine(a, b): 
#     a = a.reshape(1, -1)
#     b = b.reshape(1, -1)
#     return cosine_similarity(a, b)

def get_target(id_req, flow):
    filename = 'medy-sample-dataset.csv'
    df = pd.read_csv(filename)

    if flow:
        data = list(df[~df['label_id'].isin([id_req])]['indications_and_usage'].values)
        id_data = {i: id for i, id in enumerate(list(df[~df['label_id'].isin([id_req])]['label_id'].values))}
        target = list(df[df['label_id']==id_req]['indications_and_usage'].values)

    else:  
        data = list(df['indications_and_usage'].values)
        id_data = {i: id for i, id in enumerate(list(df['label_id'].values))}
        target = [id_req]

    return df, data, id_data, target 

def recommend(id_req, flow): 
    df, data, id_data, target = get_target(id_req, flow)
    
    vocab = get_vocab()
    cv = CountVectorizer(binary=True)
    cv.fit(vocab)
    print(cv.get_feature_names())
    # --------------------------------------------------------------------------------------------------

    data_vec = cv.transform(data).toarray()
    target_vec = cv.transform(target).toarray()

    if flow:
        n = 500 
    else:
        n = 501
    
    top = 10 

    print('datavec', data_vec[0], data_vec[0].shape)
    print('targ', target)
    print('trgvec', target_vec[0], target_vec[0].shape)

    # result = {id_data[i]: cosine(data_vec[i], target_vec[0])[0][0] for i in range(n-1)}
    result = {id_data[i]: precision_score(target_vec[0], data_vec[i], average='binary', zero_division=0) for i in range(n-1)}

    print(result)
    
    result_id = sorted(result, key=result.get, reverse=True)[:top]

    # print('target:', df[df['label_id']==id_req]['indications_and_usage'].values)
    # print(df[df.label_id.isin(result_id)]['indications_and_usage'].values)

    
    dict_res = df[df.label_id.isin(result_id)].to_dict('records')

    # print(dict_res)

    return dict_res

# recommend(upc_req)


    # print(data_vec.shape)
    # print(target_vec.shape)

    # print(data_vec[0])
    # print(target_vec[0])
    
        # top10_upc = ['12312', '321321321', '12312312', '12312312312', '321321312']

    # return top10_upc