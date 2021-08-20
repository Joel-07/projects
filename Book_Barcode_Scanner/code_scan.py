import socket
import requests
from lxml import html
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host="192.168.29.192"
port=1234

s.bind((host,port))
s.listen()

def receiver(conn):
    while True :
        try:
            data=conn.recv(1024)
            dat=data.decode()
            d=dat.rstrip('@')
            url="https://www.biblio.com/"+d

            info=requests.get(url).text
            tree=html.fromstring(info)

            name=tree.xpath('//span[@class="title"]/text()')
            author=list(map(str,tree.xpath('//span[@class="author"]/text()')))

            all_data=list(zip(name,author))
            if all_data!=[]:           
                print("The name and author of the book",all_data) 
        except:
            break



def sender(conn):
        conn.send("Connected".encode())
        print("Waiting to recieve data from phone")

if __name__=="__main__":
    print("Type Ctrl+C to exit")

    while True:
        conn,addr=s.accept()
        th1 = Thread(target=receiver, args=(conn,))
        th1.start()
        th2 = Thread(target=sender, args=(conn,))
        th2.start()




        

      
      
