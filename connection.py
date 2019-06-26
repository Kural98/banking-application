__author__ = 'user'

import cx_Oracle
con = cx_Oracle.connect("system/system@localhost/xe")
cur = con.cursor()
