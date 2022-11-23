import sqlite3
import json
import re

#Opens database connection, in this case creates one as a file using sqlite
conn = sqlite3.connect("plato_database.db")

cur = conn.cursor()


js1 = json.load(open("data_sets\\salary_survey-1.json", encoding ="utf8"))
js2 = json.load(open("data_sets\\salary_survey-2.json", encoding ="utf8"))
js3 = json.load(open("data_sets\\salary_survey-3.json", encoding ="utf8"))

#Inserts records from first json file
for record in js1:
  cur.execute("SELECT role_id FROM role WHERE role =(?)", (record["Job title"],))
  role_id = int
  role_id = cur.fetchone()[0]

  cur.execute("SELECT industry_id FROM industry WHERE industry =(?)", (record["What industry do you work in?"],))
  industry_id = int
  industry_id = cur.fetchone()[0]

  age_range = str
  age_range = record["How old are you?"]

  annual_salary = str
  annual_salary = record["What is your annual salary?"]

  currency = str
  currency = record["Please indicate the currency"]

  location = str
  location = record["Where are you located? (City/state/country)"]

  #Exceptions to handle issue where some indexs are empty due to not having a city, state or country
  try:
    city = re.split(', |/|^. ', location)[0]
  except IndexError:
      city = "N/A"
  try:
    state = re.split(', |/|^. ', location)[1]
  except IndexError:
    state = "N/A"
  try:
    country = re.split(', |/|^. ', location)[2]
  except IndexError:
    country = "N/A"

  cur.execute("INSERT INTO employee(age_range, industry_id, role_id, annual_salary, currency, city, state, country) VALUES(?,?,?,?,?,?,?,?)", (age_range, industry_id, role_id, annual_salary, currency, city, state, country))

#Inserts records from second json file
for record in js2:
  cur.execute("SELECT role_id FROM role WHERE role =(?)", (record["Job Title In Company"],))
  role_id = int
  role_id = cur.fetchone()[0]

  cur.execute("SELECT industry_id FROM industry WHERE industry =(?)", (record["Industry in Company"],))
  industry_id = int
  industry_id = cur.fetchone()[0]

  age_range = str
  age_range = "N/A"

  annual_salary = str
  annual_salary = record["Total Base Salary in 2018 (in USD)"]

  currency = str
  currency = "USD"

  city = str
  try:
    city = record["Primary Location (City)"]
  except IndexError:
    city = "N/A"

  state = str
  state = "N/A"

  country = str
  try:
    country = record["Primary Location (Country)"]
  except IndexError:
    country = "N/A"

  cur.execute("INSERT INTO employee(age_range, industry_id, role_id, annual_salary, currency, city, state, country) VALUES(?,?,?,?,?,?,?,?)", (age_range, industry_id, role_id, annual_salary, currency, city, state, country))

#Inserts records from third json file
for record in js3:
  cur.execute("SELECT role_id FROM role WHERE role =(?)", (record["Job Title"],))
  role_id = int
  role_id = cur.fetchone()[0]

  industry_id = int
  industry_id = 0

  age_range = str
  age_range = "N/A"

  annual_salary = str
  try:
    annual_salary = record["Annual Base Pay"]
  except IndexError:
    annual_salary = "N/A"

  currency = str
  currency = "USD"

  city = str
  city = "N/A"

  state = str
  state = "N/A"

  country = str
  country = "N/A"
  
  cur.execute("INSERT INTO employee(age_range, industry_id, role_id, annual_salary, currency, city, state, country) VALUES(?,?,?,?,?,?,?,?)", (age_range, industry_id, role_id, annual_salary, currency, city, state, country))

conn.commit()