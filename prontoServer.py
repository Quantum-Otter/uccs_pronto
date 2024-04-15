from flask import Flask, request
import sqlite3 as sql
import os;


app = Flask(__name__)

x = ":)"



@app.route("/", methods = ["GET","POST"])
def donation_occured():
    global x
    if(request.method == "POST"):
        
        if(type(request.json["user_id"]) is int 
           and type(request.json["amount"]) is float):
            
            print(f"request data: {request.json}")
            
            x = request.json["amount"]

            ## PUT DATA INTO DATABASE
            #submit_query(f"INSERT INTO donators (user_id, donation_amount) values ({request.json["user_id"]},{request.json["amount"]})")

        else:
            print("Request not in propper form")
        return ""
    
    elif(request.method == "GET"):
        display_string = ""

        ## GET DONATIONS BY USER FROM DATABASE
        #value = submit_query("SELECT user_id, SUM(donation_amount) from donators GROUP BY user_id ORDER BY user_id")

        #for (user_id, donation_amount) in value:
        #    display_string += f"<div>Sum of user {user_id}: {donation_amount}<div>\n"
        
        ## GET TOTAL SUM FROM DATABASE
        #value = submit_query("SELECT SUM(donation_amount) from donators")

        #display_string += f"<br><div>Total Sum: {value[0][0]}<div>"

        return f"{x}"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)

'''
@app.route("/detailed-report", methods = ["GET"])
def display_donations():
    
    id = request.args.get('id')

    id_button = get_id_button(id)
    
    donation_table = get_donation_table(id)

    return  f"<div> Donation information for User {id} <div>" + donation_table + id_button
'''

'''
def submit_query(query):
    global conn

    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()

    conn.commit()
    cur.close()

    return result
'''


#def get_donation_table(id):
#    
#    hdr = '''<table>
#                        <tr>
#                        <th>Amount</th>
#                        <th>Time</th>
#                        </tr>'''
#    rows = ""
#    tail = '</table>'
#    result = submit_query(f"SELECT donation_amount, donation_time FROM donators WHERE user_id = {id} ORDER BY donation_time")

#    for (donation_amount, donation_time) in result:
#            rows += f'''<tr>
#                            <td>{donation_amount}</td>
#                            <td>{donation_time}</td>
#                        </tr>'''
#
#    return hdr + rows + tail  
#
#def get_id_button(id):
#
#   hdr = '''<form action="/detailed-report" method="get">
#                <select name="id">'''
#    
#    options = ""

#    tail = '''</select>
#                    <input type="submit" value="Filter" />
#                </form>'''

#   result = submit_query("SELECT DISTINCT user_id FROM donators ORDER BY user_id")

#    for (user_id,) in result:
#        if(int(user_id) != int(id)):
#            options += f"<option value={user_id}>{user_id}</option>"
#        else:
#            options += f"<option value={user_id} selected >{user_id}</option>"

#    return hdr + options + tail