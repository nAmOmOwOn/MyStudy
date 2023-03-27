from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 200:
        results[website] = "OK"
    elif response.status_code >= 300:
        results[website] = "OK"
    elif response.status_code >= 400:
        results[website] = "Not OK"
    elif response.status_code >= 500:
        results[website] = "Bad"
    else:
        results[website] = "FAILD"
        
print(results)