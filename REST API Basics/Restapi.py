from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    message = f"Hello, {name}!"
    return jsonify({"message": message})

if __name__=="__main__":
    app.run()


