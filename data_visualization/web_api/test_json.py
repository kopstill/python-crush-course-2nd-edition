import requests

url = "https://hacker-news.firebaseio.com/v0/item/30551541.json"
result = requests.get(url)
json = result.json()

print(json.get('titlex'))
descendants = json.get('descendants') if json.get('descendants') else 0

print(descendants)
