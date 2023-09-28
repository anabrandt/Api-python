import db
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")  
def hello():
    return {"msg":"Hello Wordl!!"}

@app.route("/carros", methods=['GET'])
def get_all():
    return db.carros

@app.route("/carros/<int:id>", methods=['GET'])
def get_id(id):
    for car in db.carros:
        if car['id'] == id:
            return car, 200 
        
        info = {'msg': "Nao encontrado"}
        return info, 404         

@app.route("/carros",methods={POST})
def insere():
    dado = request.json
    db.carros.append(dado)
    indo = {"url": f"/carros/{dado['id']}"}

app.run(debug=True)