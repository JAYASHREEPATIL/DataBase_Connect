import mysql.connector


def insert_data(uname, passwd):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="password", database="projectdb")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO login(name, number) VALUES ("{0}","{1}");'.format(uname, passwd)
    dbcursor.execute(sql)
    mysqldb.commit()