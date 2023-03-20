from requests import get
from bs4 import BeautifulSoup


base_url = "https://www.jobkorea.co.kr/Search/?stext="

keyword = "python"

response = get(f"{base_url}{keyword}")

if response.status_code != 200:
    print("Can't request page")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("div", class_="tplPagination newVer wide")
    # if pagination == None:
        # return 1
    totalpage = pagination.find("ul")
    pages = totalpage.find_all("li")
    counts = len(pages)
    # if counts != None:
    #     return counts

    


    
        


    




