import mysql.connector

if __name__ == '__main__':
    conn = mysql.connector.connect(user='root', password='root', database='mytest', host='localhost', port=3306)
    cursor = conn.cursor()
    cursor.execute('select * from sql_function')
    for line in cursor.fetchall():
        print(line)
    cursor.close()
