from flask import flack, request, jsonify

app - Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Daily Schedule Generator!"

if __name__ == '__main__':
    app.run(debug = True)