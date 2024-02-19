from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def hello_world():
    if(request.method == "GET"):

        #KEEP THIS IN MIND FOR SMS VS APP TRANSACTIONS
        print(f"FUCK YEA {request.base_url}")
        return "<p>Hi Josh :)</p>"
    elif(request.method == "POST"):

        print(f"POSTIN TIME {request.base_url}")
        print(f"request data: {request.values["test"]}")
        return "<p>POST</p>"
    else:
        return "<p>Hello, World!</p>"


@app.route("/DEV_ONLY")
def display_my_secret():
    return "<p>My secret place >:)</p>"