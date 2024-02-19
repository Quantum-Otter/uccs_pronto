from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if(request.method == "GET"):

        #KEEP THIS IN MIND FOR SMS VS APP TRANSACTIONS
        print(f"FUCK YEA {request.base_url}")
        return "<p>Hi Josh :)</p>"
    else:
        return "<p>Hello, World!</p>"


@app.route("/DEV_ONLY")
def display_my_secret():
    return "<p>My secret place >:)</p>"