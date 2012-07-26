from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

query = """SELECT name, COUNT(name) as count FROM category
GROUP BY name ORDER BY count DESC LIMIT 20"""
cursor.execute(query)
results = cursor.fetchall()

for name, count in results:
    print count, name
