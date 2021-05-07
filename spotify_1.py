from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import seleniumwire
from fake_useragent import UserAgent
import requests
import time
from pydub import AudioSegment
import speech_recognition as sr
from PIL import Image
import base64
import os
from random_words import RandomWords
import random
from bs4 import BeautifulSoup
#from pydub.silence import split_on_silence
#from nltk.tokenize import word_tokenize
#from imageai.Classification.Custom import ClassificationModelTrainer
#coded by 81l1nm1y0r
def execute():
    global re
    ua = UserAgent()
    headers = {"User-Agent": ua.firefox}
    def proxy():
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", '127.0.0.1')
        profile.set_preference("network.proxy.socks_port", 9050)
        profile.set_preference("network.proxy.socks_remote_dns", False)
    #proxy()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", ua.chrome)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    profile.set_preference("profile.default_content_setting_values.cookies", 2)
    profile.set_preference("profile.block_third_party_cookies", True)
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    proxy = "189.113.217.35:49733"
    desired = webdriver.DesiredCapabilities.FIREFOX
    desired["proxy"] = {
    "proxyType": "manual",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
    }
    profile.update_preferences()
    driver = webdriver.Firefox()
    driver.delete_all_cookies()
    #def get_tor():
    #    session = requests.session()
    #    session.proxies = {"http": "socks5://127.0.0.1:9050",
    #                       "https": "socks5://127.0.0.1:9050"}
    #    re = session.get("http://httpbin.org/ip").json()["origin"]
    #    return re
    #print("IP:", get_tor())
    #def iter(request):
    #    params = request.params
    #    params["X-Forwarded-For"] = get_tor()
    #    request.params = params
    #driver.request_interceptor = iter
    driver.get("https://www.spotify.com/ph-en/signup/")
    def register():
            global tek
            rw = RandomWords()
            word = rw.random_word()
            best = word + word
            email = driver.find_element_by_id("email")
            tek = best + str(random.randint(0, 10000)) + str(random.randint(0, 100000))
            email.send_keys(tek + "@atmin.net")
            time.sleep(1)
            conemail = driver.find_element_by_id("confirm")
            conemail.send_keys(tek + "@atmin.net")
            print("Email: " + tek + "@atmin.net")
            passwrd = driver.find_element_by_id("password")
            passwrd = passwrd.send_keys(tek)
            print("Password:", tek)
            username = driver.find_element_by_id("displayname")
            username.send_keys(best)
            time.sleep(1)
            day = driver.find_element_by_id("day")
            day.send_keys(random.randint(1, 30))
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")).click()
            except:
                pass
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']"))).click()
            year = driver.find_element_by_id("year")
            year.send_keys("19" + str(random.randint(80, 90)))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='month']/option[text()='June']"))).click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 700);")
            el = driver.find_element_by_name("gender")
            action = ActionChains(driver)
            action.move_to_element(el).click().perform()
            teaser = ActionChains(driver)
            agree = driver.find_elements_by_id("terms-conditions-checkbox")[0]
            #driver.execute_script("arguments[0].scrollIntoView(true);", agree)
            teaser.move_to_element(agree).click().perform()

    register()
    def open_recaptcha():
            time.sleep(random.randint(3, 13))
            WebDriverWait(driver, 16).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
            WebDriverWait(driver, 16).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
            driver.switch_to.default_content()
            time.sleep(random.randint(3, 14))
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rc-audiochallenge-tdownload-link")))
    open_recaptcha()
    #print("Program was detected!")
    #time.sleep(2)
    #print("Trying again...")
    #driver.refresh()
    #register()
    #open_recaptcha()
    #execute()
    while True:
        try:
            try:
                try:
                    url = driver.find_element_by_class_name('rc-audiochallenge-tdownload-link').get_attribute('href')
                    audio_file = requests.get(url)
                    print(url)
                    with open("test.mp3", "wb") as like:
                        like.write(audio_file.content)
                    con = AudioSegment.from_mp3("test.mp3")
                    con.export("tes.wav", format="wav")
                    r = sr.Recognizer()
                    file = sr.AudioFile("tes.wav")
                    with file as text:
                        audio = r.record(text)
                    text = r.recognize_google(audio)
                    add = driver.find_element_by_id("audio-response")
                    add.send_keys(text)
                    txt = driver.find_element_by_id("recaptcha-verify-button")
                    txt.click()
                    os.remove("tes.wav")
                    os.remove("test.mp3")
                except NoSuchElementException:
                    print("Program was detected!")
                    driver.close()
                    break
            except sr.UnknownValueError:
                driver.find_element_by_id("audio-response").send_keys("wrong")
                driver.find_element_by_id("recaptcha-verify-button").click()
        except ElementNotInteractableException:
            break
    driver.switch_to.default_content()
    with open("accounts.txt", "a") as bruh:
        bruh.write(tek + "@besst.com\n")
    driver.find_element_by_xpath("//button[@class='Button-sc-8cs45s-0 jgLyVk']").click()
    #grab redirect urls
    print(driver.current_url)
    if driver.current_url == "https://www.spotify.com/ph-en/download/other/" or driver.current_url == "https://www.spotify.com/ph-en/download/windows/" or driver.current_url == "https://open.spotify.com/":
        driver.close()
def image():
        ua = UserAgent()
        headers = {"User-Agent": ua.firefox}
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", "127.0.0.1")
        profile.set_preference("network.proxy.socks_port", 9050)
        profile.set_preference("general.useragent.override", ua.chrome)
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        browser = webdriver.ChromeOptions()
        browser.add_argument("start-maximized")
        browser.add_experimental_option("excludeSwitches", ["enable-automation"])
        browser.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Firefox(profile)
        driver.get("https://www.spotify.com/ph-en/signup/")
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        url = driver.find_element_by_class_name('rc-image-tile-33').get_attribute('src')
        print(url)


        #model_trainer = ClassificationModelTrainer()
        #model_trainer.setModelTypeAsResNet50()
        #model_trainer.setDataDirectory("idenprof")
        #model_trainer.trainModel(num_objects=10, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)
        #print(model_trainer)
while True:
    execute()
