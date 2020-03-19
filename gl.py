from googlesearch import search

ip=input("What would you like to search for? ")

max_search=10
res = []
clean = []

for url in search(ip, stop=max_search):
     res.append(url)

for i in range(max_search):
    if res[i].find("gov")!=-1:
        clean.append(res[i])
    else:
        print("False "+res[i])
print(clean)