import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

class proxy:
    def get(*number):
        ua = UserAgent()
        att = []
        req = requests.get("https://sslproxies.org/", headers={"user-agent": ua.firefox})
        beat = BeautifulSoup(req.text, "html.parser")
        get = beat.find("tbody")
        try:
            for i in get.children:
                for lan in i.contents[int(number[0])]:
                    att.append(lan)
            return att
        except ValueError:
            print("proxy must be integer!", {"0": "IP address", "1": "Port", "2": "Country_code", "3": "Country", "4": "Anonymity", "5": "Google", "6": "Https", "7": "Last_checked"})
    def check(ip, port):
        ua = UserAgent()
        print("Checking...", ip)
        req = requests.get("http://httpbin.org/ip", headers={"user-agent": ua.firefox}, proxies={"http": ip, "https": ip})
        print(req)
