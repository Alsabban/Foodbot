import mysql.connector as mysql
import datetime

con = mysql.connect(host="localhost" , user="root" , password="" , db="test")


# def  getUser(user):

 #    cur =con.cursor(dictionary=True)

  #   qry = "SELECT * FROM `user` WHERE `username`= '{}'".format(user)

   #  cur.execute(qry)

    # user = cur.fetchone()

     #return user


def  save(rest_id, name):

    cur = con.cursor(dictionary=True)

    qry = "INSERT INTO `restaurants` (id , name) VALUES(%s,%s)"

    cur.execute(qry, (rest_id, name))

    con.commit()

    return True
