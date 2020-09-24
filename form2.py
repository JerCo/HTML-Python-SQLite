# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
fname = form.getvalue('firstname')
lname = form.getvalue('lastname')

import sqlite3
conn = sqlite3.connect('rp_game.db')
# cursor lets run sql commands using execute method
c = conn.cursor()

'''
c.execute("""CREATE TABLE characters (
            first_name text,
			last_name text
            )""")
'''

'''
c.execute("""
INSERT INTO characters(first_name, last_name)
VALUES (?, ?)
""", (fname, lname,))
'''


'''
c.execute("SELECT * FROM characters")

result = c.fetchall()
'''

'''
c.execute("UPDATE characters SET first_name = ? WHERE last_name = ?", (fname, lname,))
'''

'''
c.execute("Delete from characters where last_name = ?", (lname,))
'''

conn.commit()

print("""
<html>
<body>
<h1>""")

# %s is the string placeholder, and the variables are in parenthesis
print("Hello %s" % (fname,))

print("""
</h1>
</body>
</html>
""")

conn.close()