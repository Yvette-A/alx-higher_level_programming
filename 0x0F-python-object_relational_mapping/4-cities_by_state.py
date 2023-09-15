#!/usr/bin/python3

"""Lists all cities of the database hbtn_0e_4_usa,
ordered by city id."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd="8bdec442529175b959aa",
                         db=sys.argv[3])
    c = db.cursor()

    sql_query = """
    SELECT `c`.`id`, `c`.`name`, `s`.`name`
    FROM `cities` AS `c`
    INNER JOIN `states` AS `s`
    ON `c`.`state_id` = `s`.`id`
    ORDER BY `c`.`id`
    """
    c.execute(sql_query)
    for city in c.fetchall():
        print(city)
