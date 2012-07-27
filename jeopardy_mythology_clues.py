import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

query = """SELECT category.name, clue.text, clue.answer
FROM clue, category WHERE clue.category=category.id
AND category.name LIKE '%MYTHOLOGY%' LIMIT 10"""

cursor.execute(query)
results = cursor.fetchall()

print "\nExample MYTHOLOGY clues:\n"
for clue in results:
    name, text, answer = clue
    print "In the category of %s" % (name,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""

connection.close()
