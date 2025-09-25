from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Nama: Muhammad Zaki As Shidiqi<br>NPM: 5240411230"


if __name__ == '__main__':
    app.run(debug=True)