import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

print "\nExample clues:\n"
for clue in results:
    text, answer, value = clue
    print "[$%s]" % (value,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""

connection.close()
