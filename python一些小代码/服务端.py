# import socket
# import multiprocessing
# import re
# class U:
#     def __init__(self):
#         a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         a.bind(('', 10086))
#         a.listen(128)
#         dizhi = "./www"
#         while True:
#             b,c=a.accept()
#             t1 = multiprocessing.Process(target=U.send_date, args=(b,dizhi))
#             t1.start()
#             t1.join()
#             b.close()
#         a.close()
#     def send_date(b,dizhi):
#         request = b.recv(2048)
#         print(request.decode("utf-8"))
#         file_name=re.match(r"\w+ (/[^ ]*) ",request.decode("utf-8")).group(1)
#         if file_name == '/':
#             file_name = "/index.html"
#         print(file_name)
#         try:
#             file = open(dizhi + file_name, "rb")
#         except:
#             d1 = "HTTP/1.1 404 NOT Found\r\n"
#             d2 = "Server : LOL\r\n"
#             d3 = '404 not found'
#         else:
#             file_data = file.read()
#             file.close()
#             d1= "HTTP/1.1 200 OK\r\n"
#             d2 = "Server : LOL\r\n"
#             d3= file_data.decode("utf-8")
#         d = d1 +d2+ "\r\n" + d3
#         b.send(bytes(d,"utf-8"))
#         b.close()
# if __name__=='__main__':
#     u=U()
import os,time
from  multiprocessing import *
def zjc(num):
    print(num)
    print("aaaa :%d"%os.getpid())

if __name__ == "__main__":
    t = Pool(5)
    for i in range(10):
        t.apply_async(zjc,(i,))
    t.close()
    t.join()