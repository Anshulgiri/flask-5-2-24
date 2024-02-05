from flask import Flask,request
app = Flask(__name__)

@app.route("/anshul")
def print_word():
    return f"Hello, World!"

@app.route("/user") 
def print_user():
    data = request.args.get('name')
    return f"{data}"   

if __name__ == '__main__':
    app.run(host="0.0.0.0")   