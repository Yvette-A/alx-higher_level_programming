#!/usr/bin/python3
""" Displays all cities of a given state from the databace"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    sql_query = """
    SELECT * FROM `cities` as `c`
    INNER JOIN `states` as `s`
    ON `c`.`state_id` = `s`.`id`
    ORDER BY `c`.`id`
    """

    selected_values = []
    c.execute(sql_query)
    for city in c.fetchall():
        if city[4] == sys.argv[4]:
            selected_values.append(city[2])
    print(", ".join(selected_values))
