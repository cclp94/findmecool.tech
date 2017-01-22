from flask import Flask
from bot import parseForYP
app = Flask(__name__)

@app.route("/test")
def test():
    return parseForYP()

if __name__ == '__main__':
    app.run()


