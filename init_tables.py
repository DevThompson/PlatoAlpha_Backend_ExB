import sqlite3
import json

#Opens database connection, in this case creates one as a file using sqlite
conn = sqlite3.connect("plato_database.db")

cur = conn.cursor()


js1 = json.load(open("data_sets\\salary_survey-1.json", encoding ="utf8"))
js2 = json.load(open("data_sets\\salary_survey-2.json", encoding ="utf8"))
js3 = json.load(open("data_sets\\salary_survey-3.json", encoding ="utf8"))

#Transfers job titles into set to remove duplicate values
unique_role = set()
for record in js1:
  unique_role.add(record["Job title"])
for record in js2:
  unique_role.add(record["Job Title In Company"])
for record in js3:
  unique_role.add(record["Job Title"])


for job in unique_role:
    cur.execute("INSERT INTO role(role) VALUES(?)", (job,))

cur.execute("INSERT INTO role(role_id, role) VALUES (?,?)", (0,"UNKNOWN"))

unique_industry = set()
for record in js1:
    unique_industry.add(record["What industry do you work in?"])
for record in js2:
    unique_industry.add(record["Industry in Company"])

for industry in unique_industry:
  cur.execute("INSERT INTO industry(industry) VALUES(?)", (industry,))

cur.execute("INSERT INTO industry(industry_id, industry) VALUES (?,?)", (0,"UNKNOWN"))


conn.commit()

conn.close()