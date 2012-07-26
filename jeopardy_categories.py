from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

print "Example categories:\n"
for category in results:
    print category[0]

connection.close()
