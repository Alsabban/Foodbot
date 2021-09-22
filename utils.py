import mysql.connector as mysql

con = mysql.connect(host="localhost" , user="root" , password="" , db="chatbot")

def saveRest(name,rest_id):
    cur = con.cursor(dictionary=True)
    qry = "INSERT INTO 'restaurants' (name , id) VALUES(%s,%s)"
    val = (name, rest_id)
    cur.execute(qry, val)
    con.commit()
    return True
