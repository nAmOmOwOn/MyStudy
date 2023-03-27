from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

wwr = extract_wwr_jobs(keyword)
jobs = wwr

file = open(f"{keyword}.csv", "w", encoding='utf-8')
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()



