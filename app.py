from flask import Flask

app = Flask(__name__)

@app.route('/')
def add():
    result = '最愛茹茹'
    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)
