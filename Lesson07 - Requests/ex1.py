import requests

url ='https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5 '

response = requests.get(url)

with open('music_show.json','w',encoding='utf-8-sig') as f:
    f.write(response.text)
    