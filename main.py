from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json 
import pandas as pd
import recs 

def pack(i, dict_df):
    # return a dict version of csv data 
    attrs = ['id', 'category', 'entities', 'search_precision', 'brand_name', 'effective_time',
            'purpose', 'indications_and_usage', 
            'active_ingredient', 'inactive_ingredient',
            'dosage_and_administration', 'warnings']

    temp = {}
    for attr in attrs:
        if attr == 'id':
            temp[attr] = dict_df[i]['label_id']
        elif attr == 'effective_time': 
            temp[attr] = dict_df[i]['label_effective_time']
        else: 
            try: 
                temp[attr] = dict_df[i][attr]
            except:
                pass
            
    return temp 

def load_data(): 
    filename = 'results.csv'
    df = pd.read_csv(filename)
    dict_df = df.to_dict('records')
    return df, dict_df

app = Flask(__name__)
api = Api(app)
CORS(app)

class status(Resource):
    def get(self):
        try:    
            return {'data': 'medy-api is running.'}
        except(error):
            return {'data': 'an error occured during fetching api.'}

class medicine(Resource):
    def get(self, name):
        df, dict_df = load_data()
        
        if name == "all":
            result = [pack(i, dict_df) for i in range(len(dict_df))]
            return result
        else: 
            names = list(df['brand_name'])
            req = name.lower()
            show = [] 
            
            for i, name in enumerate(names): 
                if req in name.lower(): 
                    show.append(pack(i, dict_df))

            return show[:10]

class details(Resource):
    def get(self, id): 
        df, dict_df = load_data()
        
        for i in range(len(df)):
            if dict_df[i]['label_id'] == id:
                return [pack(i, dict_df)]

class keywords(Resource):
    def get(self, key):
        vocab = recs.get_vocab()
        res = [cat for cat in vocab.keys() if cat[0]==key]
        result = [{'category': cat} for cat in res] 
        return result

class conditions(Resource):
    def get(self, cat):
        vocab = recs.get_vocab()
        result = [{'condition': con} for con in vocab[cat]] 
        return result            

class recommend1(Resource): 
    def get(self, id):
        by_id = True
        dict_res = recs.recommend(id, by_id) 
        return [pack(i, dict_res) for i in range(len(dict_res))]

class recommend2(Resource): 
    def get(self, conditions):
        by_id = False
        dict_res = recs.recommend(conditions, by_id) 
        return [pack(i, dict_res) for i in range(len(dict_res))]

api.add_resource(status, '/')
api.add_resource(medicine, '/medicine/<name>')
api.add_resource(details, '/details/<id>')
api.add_resource(keywords, '/keywords/<key>') # return category by alphabet 
api.add_resource(conditions, '/conditions/<cat>') # return condition by category 
api.add_resource(recommend1,'/recommend1/<id>') 
api.add_resource(recommend2,'/recommend2/<conditions>') 

if __name__ == '__main__':
    app.run()