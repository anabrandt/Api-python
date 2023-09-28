import db
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")  
def hello():
    return {"msg":"Hello Wordl!!"}

@app.route("/carros", methods=['GET'])
def get_all():
    return db.carros

def get_id(id):
    for car in db.carros:
        if car['id'] == id:
            return car 

app.run(debug=True)