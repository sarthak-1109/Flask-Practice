from flask import Flask,request,render_template,json,jsonify # type: ignore

import os
import pymongo # pyright: ignore[reportMissingImports]


##load_dotenv()
#MONGO_URI=os.getenv('MONGO_URI')


client=pymongo.MongoClient('mongodb+srv://dummy:1234@practice.suvswjt.mongodb.net/?appName=Practice')

db=client.test    #This is a test database

collection=db['flask_tutorial']


app=Flask(__name__)

@app.route('/')

def home():

    return render_template('index.html')
 
@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)    #This form_data should be a dictionary type

    email=request.form['email']
    if not email:
        return "All fields are required"

    return "Data Submitted Succesfully"

@app.route('/api')
def get_data():
    file=open('data.json','r')    #opens the file data.json
    data=json.load(file)    
    return jsonify(data)


@app.route('/view')
def view():
    data=collection.find()   #Data is a cursor of objects i.e. a list
    data=list(data)
    for item in data:
        print(item)
        
        del item['_id']
    data={
        'data':data      #Converting into dictionary
    }
    print(data)
    return data
if __name__=='__main__':
    app.run(debug=True)
    