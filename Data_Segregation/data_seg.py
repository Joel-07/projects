d1,d2={},{}
with open('Category.txt','r') as car:
    for i in car:
        g,h=i.strip('\n').split(':')
        d1[g.strip()]=h.strip()
        
with open('data1.txt') as data:
    for i in data:
        a=(i.strip('\n').split("\t",-1))
        d2[a[0].strip()]=a[-1].strip()

def comp(d1,d2):
    for a,b in d1.items():
        for j in list(d2):
            if a in j:
                with open(str(b)+'.txt','a') as wr:
                    wr.write(j+' '+d2[j]+'\n')
                    del[d2[j]]

comp(d1,d2)
for i,j in d2.items():
    with open('extra.txt','a') as wr:
        wr.write(i+' '+j+'\n')
