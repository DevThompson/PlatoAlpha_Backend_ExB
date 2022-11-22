import sqlite3

#Opens database connection, in this case creates one as a file using sqlite
conn = sqlite3.connect("plato_database.db")

cur = conn.cursor()

#Creates table
cur.execute("CREATE TABLE IF NOT EXISTS employee(employee_id INTEGER PRIMARY KEY, age_range, industry_id NOT NULL, role_id NOT NULL, annual_salary, currency, city, state, country)")
cur.execute("CREATE TABLE IF NOT EXISTS role(role_id INTEGER PRIMARY KEY, role UNIQUE)")
cur.execute("CREATE TABLE IF NOT EXISTS industry(industry_id INTEGER PRIMARY KEY, industry UNIQUE)")

#Closes connection
conn.close