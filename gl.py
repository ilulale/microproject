from googlesearch import search

def cleaner(res):
    clean=[]
    file=open("trustlist.txt","r")
    trustlist=[l.strip() for l in file.readlines()]
    print(trustlist)
    file.close()
    for x in range(len(trustlist)):
        for i in range(len(res)):
            if res[i].find(trustlist[x])!=-1:
                clean.append(res[i])
            else:
                continue
    return clean

ip=input("What would you like to search for? ")

max_search=1000
res = []
clean = []
user_agnt = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

for url in search(ip, stop=max_search,user_agent= user_agnt,country='india'):
     res.append(url)

clean=cleaner(res)
tot=0
for  i in range(len(clean)):
    print(clean[i])
    tot=tot+1

print(str(tot)+"Trusted sources")