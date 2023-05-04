from jobkorea import*

keyword = "python" # 키워드 설정 가능!

mjob = extract_jobkorea_jobs(keyword)

file = open(f"{keyword}.csv", "w")

file.write("company,title,exp,link,edu,location\n")

for job in mjob:
    file.write(f"{job['company']},{job['title']},{job['exp']},{job['link']},{job['edu']},{job['location']}\n")

file.close()
