from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return"Trying to run NLP model"

if __name__== '__main__':
    print("Name of file is:", __name__)
    app.run(debug=True)