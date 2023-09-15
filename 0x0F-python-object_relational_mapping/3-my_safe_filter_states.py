#!/usr/bin/python3
""" Displays all values in the states table
of the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for row in c.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
