import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
job_elements = soup.find_all("div", class_="card-content")

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        PRIMARY KEY (title, company, location)
    )
''')

for job in job_elements:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    apply_link = job.find("a", string="Apply")["href"]

    cursor.execute('SELECT description, apply_link FROM jobs WHERE title=? AND company=? AND location=?',
                   (title, company, location))
    existing = cursor.fetchone()

    if not existing:
        cursor.execute('INSERT INTO jobs (title, company, location, description, apply_link) VALUES (?, ?, ?, ?, ?)',
                       (title, company, location, description, apply_link))
    elif existing[0] != description or existing[1] != apply_link:
        cursor.execute('''
            UPDATE jobs
            SET description=?, apply_link=?
            WHERE title=? AND company=? AND location=?
        ''', (description, apply_link, title, company, location))

conn.commit()

def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)

    return cursor.execute(query, params).fetchall()

def export_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)

conn.close()
