import mysql.connector
def link_mysql():
    #conn = mysql.connector.connect(user='root', password='vRt5leRdr8*t', database='onlineshop8', use_unicode=True)
    conn = mysql.connector.connect(user='root', password='root', database='online_shop7', use_unicode=True)
    return conn