from flask import Flask, request

app = Flask(__name__)

total = 0

@app.route("/", methods = ["GET","POST"])
def donation_occured():

    global total

    if(request.method == "GET"):
        return f"{total}"
    

    elif(request.method == "POST"):
        
        if(type(request.json["donationAmount"]) is int ):
            print(f"request data: {request.json}")
            total += request.json["donationAmount"]
        else:
            print("SHHSH")

        return ""
    else:
        return "<p>Got through the great firewall</p>"


@app.route("/DEV_ONLY")
def display_my_secret():
    return "<p>My secret place >:)</p>"