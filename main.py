from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json 
import pandas as pd

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
        filename = 'bangkit_0323_dataset.json'
        with open(filename) as f: 
            file = json.load(f) 

            if name == "all":
                output = [file[str(i)] for i in range(len(file))] 
                return output 
            else: 
                names = [file[str(i)]['brand_name'].lower() for i in range(len(file))] 
                
                req = name.lower()
                show = [] 
                
                for i, name in enumerate(names): 
                    if req in name: 
                        show.append(file[str(i)])
    
                return show[:10]

class details(Resource):
    def get(self, id): 
        filename = 'bangkit_0323_dataset.json'
        with open(filename) as f: 
            file = json.load(f) 
        
            for i in range(len(file)):
                if file[str(i)]['id'] == id:
                    return [file[str(i)]]

class keywords(Resource):
    def get(self, key):
        filename = 'vocab.json'
        with open(filename) as f: 
            file = json.load(f)

            if key == 'all':
                return file 
            else:
                
                alphabet = 'abcdefghijklmnopqrstuvwxyz'

                for i in range(len(alphabet)):
                    if alphabet[i] == key: 
                        num = i
                        print(num)
                
                result = file[num]    

                return [result]            
                

api.add_resource(status, '/')
api.add_resource(medicine, '/medicine/<name>')
api.add_resource(details, '/details/<id>')
api.add_resource(keywords, '/keywords/<key>')

if __name__ == '__main__':
    app.run()