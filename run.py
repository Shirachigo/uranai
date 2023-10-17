from flask import Flask, jsonify, request
app = Flask(__name__) 

@app.route('/')
def hello():
    text = "Hello World!"
    return jsonify(message = text)

if __name__ == '__main__':
    app.run()