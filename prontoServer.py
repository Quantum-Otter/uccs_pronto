from flask import Flask, request
import mysql.connector;
import os;


app = Flask(__name__)

conn = mysql.connector.MySQLConnection(
    user = "root",
    password = os.getenv('MySqlPassword'),
    database="uccs_pronto"
    )
conn.autocommit = False;

@app.route("/", methods = ["GET","POST"])
def donation_occured():

    if(request.method == "GET"):
        display_string = ""
        value = submit_query("SELECT user_id, SUM(donation_amount) from donators GROUP BY user_id")

        for (user_id, donation_amount) in value:
            display_string += f"<div>Sum of user {user_id}: {donation_amount}<div>\n"
        
        value = submit_query("SELECT SUM(donation_amount) from donators")

        display_string += f"<br><div>Total Sum: {value[0][0]}<div>"

        return f"{display_string}"
    

    elif(request.method == "POST"):
        
        if(type(request.json["user_id"]) is int 
           and type(request.json["amount"]) is float):
            
            print(f"request data: {request.json}")
            
            submit_query(f"INSERT INTO donators (user_id, donation_amount) values ({request.json["user_id"]},{request.json["amount"]})")

        else:
            print("SHHSH")

        return ""
    else:
        return "<p>Got through the great firewall</p>"


@app.route("/DEV_ONLY")
def display_my_secret():
    return "<p>My secret place >:)</p>"

def submit_query(query):
    global conn

    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    conn.commit()
    cur.close()

    return result
