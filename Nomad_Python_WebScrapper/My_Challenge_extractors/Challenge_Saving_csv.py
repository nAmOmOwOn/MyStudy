from jobkorea import*

keyword = "python"

mjob = extract_jobkorea_jobs(keyword)

file = open(f"{keyword}.csv", "w")

file.write("title,exp,link,edu,location\n")

for job in mjob:
    file.write(f"{job['title']},{job['exp']},{job['link']},{job['edu']},{job['location']}\n")

file.close()
