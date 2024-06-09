from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "VIJAY G BOLTHEY..."

if __name__ == '__main__':
    app.run(debug=True)
