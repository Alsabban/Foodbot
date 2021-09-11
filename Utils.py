import mysql.connector as mysql
import datetime

con=mysql.conect(host="localhost",user="root",password="",db="coursebot")


def  getUser(user):

    cur =con.cursor(dictionary=True)

    qry = "SELECT * FROM `user` WHERE `username`= '{}'".format(user)

    cur.execute(qry)

    user = cur.fetchone()

    return user


def  save(user_id):

    cur = con.cursor(dictionary=True)

    qry = "INSERT INTO `user_attendance` (user_id , date) VALUES(%s,%s)"

    cur.execute(qry, (user_id, datetime.datetime.now()))

    con.commit()

    return True