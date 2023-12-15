#!/usr/bin/python3
"""  lists all the states from the database called hbtn_0e_0_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    currt = dtb.cursor()
    currt.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rowws = currt.fetchall()
    tempr = list(one_row[0] for one_row in rowws)
    print(*tempr, sep=", ")
    currt.close()
    dtb.close()
