f = open('ip.txt', 'r')
iplist = f.readlines()
 
for ip in iplist:
    print(ip)
f.close()