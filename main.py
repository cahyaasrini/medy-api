from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json 
import pandas as pd

# import recs 

app = Flask(__name__)
api = Api(app)
CORS(app)

class status(Resource):
    def get(self):
        try:    
            return {'data': 'medy-api is running'}
        except(error):
            return {'data': 'an error occured during fetching api'}

class medicine(Resource):
    def get(self, name):
        if name == "all":
            result = [pack(i) for i in range(len(df))]
            return result
        else: 
            names = list(df['brand_name'])
            req = name.lower()
            show = [] 
            
            for i, name in enumerate(names): 
                if req in name.lower(): 
                    show.append(pack(i))

            return show[:10]

class details(Resource):
    def get(self, id): 
        for i in range(len(df)):
            if dict_df[i]['label_id'] == id:
                return [pack(i)]

class keywords(Resource):
    def get(self, key):
        vocabfile = 'vocab.json'
        with open(vocabfile) as f: 
            file = json.load(f)

            if key == 'all':
                return file 
            else:
                
                alphabet = 'abcdefghijklmnopqrstuvwxyz'

                for i in range(len(alphabet)):
                    if alphabet[i] == key: 
                        num = i
                        print(num)
                
                result = file[num][key]    

                return result # no need []            

def pack(i):
    attrs = ['id', 'category', 'brand_name', 'effective_time',
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
            temp[attr] = dict_df[i][attr]

    return temp 

 
                 


api.add_resource(status, '/')
api.add_resource(medicine, '/medicine/<name>')
api.add_resource(details, '/details/<id>')
api.add_resource(keywords, '/keywords/<key>')
# api.add_resource(recommend,'/recommend/<string:upc>')

if __name__ == '__main__':
    # filename = 'bangkit_0323_dataset.json'
    filename = 'medy-sample-dataset.csv'
    df = pd.read_csv(filename)
    dict_df = df.to_dict('records')
    app.run()