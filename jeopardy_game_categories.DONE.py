import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
game_id = results[0][0]
print "Categories for game #%d:" % (game_id,)

# Simplest is:
#     "SELECT name FROM category WHERE game=%d" % (game_id,),
# but it's nice to highlight the rounds.

query = """SELECT name, round FROM category
WHERE game=%d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    # round 0 = Jeopardy round
    # round 1 = Double Jeopardy round
    # round 2 = Final Jeopardy
    name, round = result
    print round, name
