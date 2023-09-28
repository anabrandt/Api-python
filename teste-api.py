

from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")  
def hello():
    return {"msg":"Hello Wordl!!"}

app.run(debug=True)