#!/var/www/cgi-bin/bin/python3

import psycopg2
import sys
import json

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(user='alex', dbname="base1",  password='inspirion', host='localhost')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')

conn.autocommit = True
 
# Creating a cursor object
cursor = conn.cursor()

# получаем все данные из таблицы people
cursor.execute("SELECT * FROM table2;")

list_1 = cursor.fetchall()
json_str = json.dumps(list_1, ensure_ascii=False, default=str)

print("Content-type: application/json", end="\r\n\r\n", flush=True)
sys.stdout.buffer.write(bytes(json_str,encoding='utf8'))

cursor.close()
conn.close()



