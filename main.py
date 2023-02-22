from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def wa_hello():
    return "Hello, World!"


@app.route("/piyush")
def piyush_hello():
    return "Hello, World Piyush Jha!"
 
if __name__ == "__main__":
    app.run(debug=True)
