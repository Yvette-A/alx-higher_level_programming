#!/usr/bin/python3

""" Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd="8bdec442529175b959aa",
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
