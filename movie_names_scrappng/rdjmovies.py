import requests
from lxml import html
from threading import Thread
import csv

url = "https://m.imdb.com/name/nm0000375/filmotype/actor"
data = requests.get(url).text
tree = html.fromstring(data)
url1 = tree.xpath('//div[@class="col-xs-12 col-md-6"]//a/@href')
nm, rating,l1 = [],[],[]

def imdb(u):
    try:
        nurl = "https://m.imdb.com/"
        ur = nurl+u
        d = requests.get(ur).text
        tr = html.fromstring(d)
        name = tr.xpath('//h1/text()')
        rate = tr.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()')
        if rate != []:
            nm.append(name[0])
            rating.append(rate[0])
    except Exception as e:
        print(e)

print("Collecting Data")
for i in url1:
    th1 = Thread(target=imdb, args=(i,))
    th1.start()
    l1.append(th1)
for j in l1:
    j.join()

alld = list(zip(nm, rating))

new_csv = "mnames.csv"
with open(new_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(alld)
