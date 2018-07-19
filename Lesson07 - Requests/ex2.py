import json

with open('music_show.json',encoding='utf-8-sig') as m:
    f= json.load(m)
    
    with open('music_show.txt','w',encoding='utf-8-sig' )as n:
        for i in f:
            a='{0:20}'.format(i['title'])+'{0:>10}'.format(i['startDate'])+'~'+'{0:10}'.format(i['endDate'])+'\n'
            
            n.write(a)
