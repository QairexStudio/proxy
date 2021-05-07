import requests
import proxy as test

ip, port, last_checked = [], [], []
for i in test.proxy.get(0):
    ip.append(i)
for t in test.proxy.get(1):
    port.append(t)
for _ in test.proxy.get(7):
    last_checked.append(_)
print(str(ip[0]) + ":" + str(port[0]) + " Last_checked ==> " + str(last_checked[0]))
print("-----------------SELECT--------------ALL----------------TABLES----------------")
for i in range(len(ip)):
    print(str(ip[i]) + ":" + str(port[i]) + " Last_checked ==> " + str(last_checked[i]))
print("-------------------GET-----------------ALL---------------------DATA----------------")
for u in range(7):
    print(test.proxy.get(u))
test.proxy.check(ip[0], port[0])
