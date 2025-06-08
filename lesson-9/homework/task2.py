import csv
from collections import defaultdict


grades = []
with open('grades.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)


subject_totals = defaultdict(list)

for entry in grades:
    subject = entry['Subject']
    grade = entry['Grade']
    subject_totals[subject].append(grade)

averages = {subject: sum(grades)/len(grades) for subject, grades in subject_totals.items()}


with open('average_grades.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, avg in averages.items():
        writer.writerow([subject, round(avg, 1)])