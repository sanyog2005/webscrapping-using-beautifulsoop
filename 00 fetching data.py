import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
        
url="https://timesofindia.indiatimes.com/india/delhi-chief-minister-arvind-kejriwal-interim-bail-live-updates-jail-lok-sabha-elections-supreme-court-aap-atishi-bharatiya-janata-party-bjp-congress-cm/liveblog/110024060.cms"

fetchAndSaveToFile(url, "data/times.html")

