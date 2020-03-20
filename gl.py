from googlesearch import search

def opener():
    file=open("trustlist.txt","r")
    trustlist=[l.strip() for l in file.readlines()]
    file.close()
    return trustlist

def new_clean(url,trustlist,clean):
    
    if url!=1:
        for x in range(len(trustlist)):
            if url.find(trustlist[x])!=-1:
                clean.append(url)
    else:
        return clean


ip=input("What would you like to search for? ")

max_search=100
res = []
clean = []
user_agnt = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

trustlist = opener()
for url in search(ip, stop=max_search,user_agent= user_agnt,country='india'):
     res.append(url)
     print(url)
     new_clean(url,trustlist,clean)

clean = new_clean(1,trustlist,clean)
tot=0
print("----------------#################-----------------------------")
print("----------------#################-----------------------------")
print("----------------#################-----------------------------")
print("\tPrinting tursted sources")
for  i in range(len(clean)):
    print(clean[i])
    tot=tot+1

print(str(tot)+"Trusted sources")