from requests import get
from bs4 import BeautifulSoup



results = []

keyword = "python"

base_url = "https://www.jobkorea.co.kr/Search/?stext="
final_url = f"{base_url}{keyword}&tabType=recruit&Page_No="

response = get(final_url)

if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text,"html.parser")
    total = soup.find("div", class_="lists-cnt dev_list")
    jobs = total.find_all("li", class_="list-post")
    for job in jobs:
        job_post = job.find("div", class_="post")
        job_company = job_post.find("div", class_="post-list-corp")
        job_info = job_post.find("div", class_="post-list-info")
        company_info = job_company.find("a")
        info = job_info.find("a")
        info_URL = info['href']
        company_title = company_info['title']
        info_title = info['title']
        info_title = info_title.replace(","," ")

        info_detail = job_info.find("p", class_="option")
        info_exp = info_detail.find("span", class_="exp").string
        info_exp = info_exp.replace(",", " ")
        if info_detail.find("span", class_="edu") == None:
            info_edu = info_detail.find("span", class_="edu") == "없음"
        else:
            info_edu = info_detail.find("span", class_="edu").string
        info_loc = info_detail.find("span", class_="loc long").string
        info_loc = info_loc.replace(",", " ")
        
        job_data = {
            "title" : info_title,
            "exp" : info_exp,
            "link" : f"https://www.jobkorea.co.kr{info_URL}",
            "edu" : info_edu,
            "location" : info_loc
        }
        results.append(job_data)


for result in results:
    print(result)
    print("///////////////////")

