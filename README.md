# proxy
sslproxies.com scraper

### USAGE

Usage of the library has all examples in test.py file, easy and simple to use but let's explain in detail.

Function | what is it for 
------------ | -------------
proxy | Proxy class 
get | get data from sslproxies.com
check | proxy tested

### Packages used

* fake-useragent
* beautifulsoup4
* requests

Don't forget to put the library in the directory where your file is located.

#### include it in your project or program

```py
import proxy as test
```

### Let's pull the data
```py
ip, port = [], []
for i in test.proxy.get(0):
  ip.append(i)
for t in test.proxy.get(1):
  port.append(t)
print(str(ip[0]) + ":" + str(port[0]))
```
Result:

```py
219.92.3.149:8080
```

### Check the Proxy connection

```py
ip, port = [], []
for i in test.proxy.get(0):
  ip.append(i)
for t in test.proxy.get(1):
  port.append(t)
test.proxy.check(ip[0], port[0])
```
Result:

```py
Working...169.57.1.84:8123
```

### get all the information

```py
att = []
for t in range(7):
  att.append(test.proxy.get(t))
print(att)
```

Result:

```py
['169.57.1.84', '103.87.169.243', '161.202.226.194', '132.248.196.2', '103.152.5.70', '20.151.27.156', '216.21.18.194', '103.103.175.253', '198.50.163.192', '183.88.226.50', '169.57.1.85', '167.172.171.151', '219.92.3.149', '103.227.254.59', '202.61.51.204', '157.230.103.189', '54.165.67.102', '104.238.81.186', '119.81.189.194', '194.5.206.148', '18.178.146.121', '168.119.137.56', '85.15.152.39', '223.255.133.34', '115.75.1.184', '118.99.104.16', '181.3.74.175', '109.254.47.147', '167.172.180.40', '51.222.67.222', '51.222.67.215', '139.99.102.114', '51.222.67.220', '51.222.67.214', '115.124.115.26', '186.47.83.157', '103.151.125.234', '181.129.43.3', '116.80.41.12', '91.195.156.241', '114.32.84.229', '68.183.221.156', '181.129.183.19', '189.199.126.94', '20.195.17.90', '41.162.186.2', '181.3.107.40', '186.126.65.181', '176.197.95.2', '103.240.77.98', '51.81.21.221', '175.100.103.132', '1.10.186.35', '37.120.192.154', '91.185.51.68', '213.230.91.75', '45.173.18.235', '54.186.85.238', '109.110.73.106', '186.219.96.47', '151.106.34.139', '129.21.95.85', '217.79.181.109', '186.4.186.36', '50.246.120.125', '90.182.166.59', '139.99.105.5', '37.111.42.210', '109.70.189.70', '181.129.138.114', '186.233.96.246', '84.214.150.146', '181.102.53.107', '109.238.222.5', '160.19.232.85', '180.179.98.22', '143.198.196.205', '103.9.188.229', '82.99.232.18', '103.250.156.22', '188.72.6.98', '115.249.2.192', '109.236.108.246', '92.223.105.32', '51.222.67.212', '95.79.55.196', '85.175.216.32', '103.251.214.167', '176.28.64.225', '109.73.181.192', '80.73.9.238', '202.92.6.226', '93.62.245.77', '182.253.173.8', '213.230.97.169', '129.226.52.93', '118.99.100.210', '45.112.124.133', '70.44.24.245', '191.7.210.162']
['8123', '55214', '80', '8080', '8080', '3128', '80', '3128', '3129', '8080', '80', '41233', '8080', '80', '3128', '36366', '8080', '56227', '80', '3128', '80', '3128', '3128', '8080', '8118', '8080', '10809', '3128', '43112', '32768', '32768', '80', '32768', '32768', '80', '8080', '3128', '8080', '80', '3128', '80', '34001', '53281', '8080', '3128', '48017', '10809', '10809', '3128', '30093', '3128', '55667', '37235', '8080', '3128', '3128', '3128', '3128', '32479', '54570', '1080', '8080', '443', '3128', '8080', '80', '80', '8080', '56408', '30838', '23500', '8080', '10809', '40387', '3128', '3128', '80', '36984', '58689', '30093', '37083', '8080', '3128', '3128', '3129', '53281', '53281', '6666', '3128', '43268', '808', '6060', '80', '8080', '3128', '443', '8080', '8080', '8888', '35820']
['MX', 'IN', 'JP', 'MX', 'ID', 'CA', 'US', 'ID', 'CA', 'TH', 'MX', 'DE', 'MY', 'ID', 'PK', 'DE', 'US', 'US', 'HK', 'NL', 'JP', 'DE', 'RU', 'HK', 'VN', 'ID', 'AR', 'UA', 'DE', 'CA', 'CA', 'SG', 'CA', 'CA', 'IN', 'EC', 'VN', 'CO', 'JP', 'UA', 'TW', 'DE', 'CO', 'MX', 'SG', 'ZA', 'AR', 'AR', 'RU', 'IN', 'US', 'KH', 'TH', 'NL', 'RU', 'UZ', 'AR', 'US', 'UA', 'BR', 'FR', 'US', 'DE', 'EC', 'US', 'CZ', 'SG', 'MM', 'RU', 'CO', 'BR', 'NO', 'AR', 'CZ', 'ZA', 'IN', 'SG', 'KH', 'IR', 'IN', 'IQ', 'IN', 'RU', 'LU', 'CA', 'RU', 'RU', 'IN', 'RU', 'IT', 'UA', 'VN', 'IT', 'ID', 'UZ', 'HK', 'ID', 'ID', 'US', 'BR']
['Mexico', 'India', 'Japan', 'Mexico', 'Indonesia', 'Canada', 'United States', 'Indonesia', 'Canada', 'Thailand', 'Mexico', 'Germany', 'Malaysia', 'Indonesia', 'Pakistan', 'Germany', 'United States', 'United States', 'Hong Kong', 'Netherlands', 'Japan', 'Germany', 'Russian Federation', 'Hong Kong', 'Vietnam', 'Indonesia', 'Argentina', 'Ukraine', 'Germany', 'Canada', 'Canada', 'Singapore', 'Canada', 'Canada', 'India', 'Ecuador', 'Vietnam', 'Colombia', 'Japan', 'Ukraine', 'Taiwan', 'Germany', 'Colombia', 'Mexico', 'Singapore', 'South Africa', 'Argentina', 'Argentina', 'Russian Federation', 'India', 'United States', 'Cambodia', 'Thailand', 'Netherlands', 'Russian Federation', 'Uzbekistan', 'Argentina', 'United States', 'Ukraine', 'Brazil', 'France', 'United States', 'Germany', 'Ecuador', 'United States', 'Czech Republic', 'Singapore', 'Myanmar', 'Russian Federation', 'Colombia', 'Brazil', 'Norway', 'Argentina', 'Czech Republic', 'South Africa', 'India', 'Singapore', 'Cambodia', 'Iran', 'India', 'Iraq', 'India', 'Russian Federation', 'Luxembourg', 'Canada', 'Russian Federation', 'Russian Federation', 'India', 'Russian Federation', 'Italy', 'Ukraine', 'Vietnam', 'Italy', 'Indonesia', 'Uzbekistan', 'Hong Kong', 'Indonesia', 'Indonesia', 'United States', 'Brazil']
['elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'anonymous', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'anonymous', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'anonymous', 'elite proxy', 'anonymous', 'anonymous', 'elite proxy', 'anonymous', 'anonymous', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'anonymous', 'anonymous', 'elite proxy', 'elite proxy', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy', 'elite proxy', 'anonymous', 'elite proxy']
['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']
['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes']
```

### Index numbers

```py
test.proxy.get("test")
```

Result:

```py
proxy must be integer! {'0': 'IP address', '1': 'Port', '2': 'Country_code', '3': 'Country', '4': 'Anonymity', '5': 'Google', '6': 'Https', '7': 'Last_checked'}
```

### you can also separate

```py
ip, port = [], []
for i in test.proxy.get(0):
  ip.append(i)
for t in test.proxy.get(1):
  port.append(t)
if test.proxy.check(ip[0], port[0]):
  print("Connection established")
```

Result

```py
Connection established
```

### Errors

* Not working: proxy does not work
* Working: proxy is working
* Proxy cannot connect: the proxy server is too slow or faulty server i.e. the server cannot be reached
* Proxy Connection Timeout: proxy server too slow or faulty server
* Proxy ERROR: bad proxy not well configured or proxy with problem


--------

## Knowledge

This program was originally created as a utility of a program and has been published for this purpose. The use of the program depends on the person. besides, the program was not seriously created. that is, it was created for entertainment purposes and donated to software developers. It is completely free to develop the program.

If you are a developer, you can contact us: QairexStudio@gmail.com
