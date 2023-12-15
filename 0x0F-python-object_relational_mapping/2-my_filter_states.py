#!/usr/bin/python3
"""  lists all the states from the database called hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    currt = dtb.cursor()
    currt.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rowws = currt.fetchall()
    for one_row in rowws:
        print(one_row)
    currt.close()
    dtb.close()
