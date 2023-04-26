from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>WELCOME TO TURAN CYBER HUB</h1>"  \
           "<h2>Git Class Hands On</h2>"
@app.route('/home')
def home():
    return "<h1>Welcome home<h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
