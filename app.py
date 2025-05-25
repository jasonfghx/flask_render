from flask import Flask

app = Flask(__name__)

@app.route('/')
def add():
    result = 1 + 1
    return f'1 + 1 = {result}'

if __name__ == '__main__':
    app.run(debug=True)
