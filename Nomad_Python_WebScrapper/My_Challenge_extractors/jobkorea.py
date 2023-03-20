from requests import get
from bs4 import BeautifulSoup

def get_page(keyword):

    base_url = "https://www.jobkorea.co.kr/Search/?stext="

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request page")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("div", class_="tplPagination newVer wide")
        if pagination == None:
            return 1
        totalpage = pagination.find("ul")
        pages = totalpage.find_all("li")
        counts = len(pages)
        if counts != None:
            return counts

def extract_jobkorea_jobs(keyword):

    pages = get_page(keyword)
    results = []
    for page in pages:
        base_url = "https://www.jobkorea.co.kr/Search/?stext="
        final_url = f"{base_url}{keyword}&tabType=recruit&Page_No={page}"

        response = get(final_url)

        if response.status_code != 200:
            print("Can't request website")
        else:
            soup = BeautifulSoup(response.text,"html.parser")
            total = soup.find("div", class_="lists-cnt dev_list")
            jobs = total.find_all("li", class_="list-post")
            for job in jobs:
                job_post = job.find("div", class_="post")
                job_info = job_post.find("div", class_="post-list-info")
                info = job_info.find("a")
                info_URL = info['href']
                info_title = info['title']

                info_detail = job_info.find("p", class_="option")
                info_exp = info_detail.find("span", class_="exp").string
                info_edu = info_detail.find("span", class_="edu").string
                info_loc = info_detail.find("span", class_="loc long").string
                
                job_data = {
                    "title" : info_title,
                    "exp" : info_exp,
                    "link" : f"https://www.jobkorea.co.kr{info_URL}",
                    "edu" : info_edu,
                    "location" : info_loc
                }
                results.append(job_data)


