# Notes
- This is for educational purposes only as it is illegal.
- You can try the code on your own network or website.
- This script is very basic and inefficient.
- Join my [Discord Server](https://discord.com/invite/VNAQrkQ) for support.
- My [website](https://oblivionghoul.com/).
- For more info on DDOS Attacks, view this [document](https://its.fsu.edu/sites/g/files/imported/storage/original/application/dfd40f8b7415faa8fc306afa529520da.pdf).

# Setup (DOS)
1. Download the code and edit the python document.
2. Enter the target ip, the port, and the fakeip.
```
target = '' (Insert the target ip or a domain name [ex: target = '10.3.5.23'])
port =  (Insert the port [ex: port = 22]) Port 22: DOS the SSH servers, Port 80: DOS the HTTP servers
fake_ip = '' Insert your fake ip here (note: this will not prevent you from getting caught) (ex: fake_ip = '10.4.3.35')
```
3. Decide if you want to log how many times the code is ran (this will slow down the script).
```
Delete the hashtag in front of these lines if you want to log how many times the code is ran
#global connectedCount
#connectedCount += 1
#print(connectedCount)
```
4. Decide how many threads you want to run.
```
for i in range(10): (Change the number 10 to how many threads you want to run) (ex: for i in range(100):)
```
5. Save the document and run the python code.

# Contributions
All contributions are welcome. This is just a basic script, so there are many things to improve on.
