from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json 

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

class category(Resource):
    def get(self, cat):
        filename = 'bangkit_0323_dataset.json'
        with open(filename) as f: 
            file = json.load(f) 
            n = 10
            return [file[str(i)] for i in range(len(file)) if file[str(i)]['category'] == cat][:n]

api.add_resource(status, '/')
api.add_resource(medicine, '/medicine/<name>')
api.add_resource(details, '/details/<id>')
api.add_resource(category, '/category/<cat>')

if __name__ == '__main__':
    app.run()