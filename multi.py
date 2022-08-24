# I do not forbid you to change my name, but please don't remove the tag Powered
# This is next Generation From I-WRAH Tools
#   ______         ____  _____  ______   _______          _
# .' ____ \       |_   \|_   _||_   _ `.|_   __ \        / \
# | (___ \_| ______ |   \ | |    | | `. \ | |__) |      / _ \
#  _.____`..|______|| |\ \| |    | |  | | |  __ /      / ___ \
# | \____) |       _| |_\   |_  _| |_.' /_| |  \ \_  _/ /   \ \_
#  \______.'         |_____|\____||______.'|____| |___||____| |____|
#            Grivy Bot claim with selenium
#                            By Masbim
#               Created on Sun Ags 21 21:35:31 2020
#
#  Powered By :
#  I-WRAH Tools & T-PhuTe x & X-ReRe Scripts

 # Usage : python namescrirpt.py

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import logging
import random
import threading
import time

thread = 2
empas = [
"rosene.kauppi@niatniat.site|Admin123", 
"valera.reidar@niatniat.site|Admin123", 
"beatriz.dahlia@niatniat.site|Admin123", 
"renae.merna@niatniat.site|Admin123", 
"briney.vacuva@niatniat.site|Admin123", 
"sheelagh.mozelle@niatniat.site|Admin123", 
"misha.ophelia@niatniat.site|Admin123", 
"correy.whittaker@niatniat.site|Admin123", 
"brietta.regan@niatniat.site|Admin123", 
"dominga.hamil@niatniat.site|Admin123", 
"melodie.taima@niatniat.site|Admin123", 
"maurene.fulmer@niatniat.site|Admin123", 
"elvira.alwin@niatniat.site|Admin123", 
"gilda.borrell@niatniat.site|Admin123", 
"vita.jehu@niatniat.site|Admin123", 
"sallie.regan@niatniat.site|Admin123", 
"antonietta.dalli@niatniat.site|Admin123", 
"stevana.shelba@niatniat.site|Admin123", 
"sharai.quinn@niatniat.site|Admin123", 
"dania.joeann@niatniat.site|Admin123", 
"anica.aaberg@niatniat.site|Admin123", 
"nyssa.ludewig@niatniat.site|Admin123", 
"wileen.buffum@niatniat.site|Admin123", 
"ivett.byrne@niatniat.site|Admin123"
]


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
        self.hits = 0
        self.bad = 0
        # self.browser = False
        # self.login = False
    def increment(self):
        self.lock.acquire()
        try:
          self.value = self.value + 1
        finally:
          self.lock.release()

def worker(c,ind, user):
  time.sleep(0.5)
  print("[PREPARING] "+user)
  lists = user.split('|')
  email = lists[0]
  password = lists[1]
  options = uc.ChromeOptions()
  # options.add_experimental_option("prefs", prefs)
  options.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 2})
  options.add_argument('--disable-notifications')
  options.add_argument('--no-sandbox')
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--disable-blink-features")
  options.add_argument("--disable-blink-features=AutomationControlled")
  options.add_argument("--disable-infobars")

  options.add_argument("--remote-debugging-port=9222")

  driver = uc.Chrome(use_subprocess=True, options=options)
  driver.set_window_size(300, 800)
  driver.set_window_position(ind, 0)
  wait = WebDriverWait(driver, 20)
  wait3s = WebDriverWait(driver, 3)
  driver.get('https://ayo.coca-cola.co.id/login/sat-coke-ayo-9-60')
  main_page = driver.current_window_handle
  wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@style,"background-color: rgb(0, 0, 0)")]')))
  try:
    driver.find_element(By.XPATH, "//*[contains(text(),'Accept all')]").click()
    print("oke")
    time.sleep(2)
  except:
    print("err")

  wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Google')]"))).click()
  for handle in driver.window_handles:
    if handle != main_page:
       login_page = handle
  driver.switch_to.window(login_page)
  time.sleep(3)
  driver.set_window_position(ind, 0)
  inputmail = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@type ="email"]')))
  inputmail.send_keys(email)
  inputmail.send_keys(Keys.RETURN)
  try:
    wait3s.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="captchaimg"]')))
    print("ene captchaimg")
    driver.quit()
  except:
    inputpass = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
    inputpass.send_keys(password)
    inputpass.send_keys(Keys.RETURN)
    try:
      wait3s.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="captchaimg"]')))
      print("ene captchaimg")
      driver.quit()
    except:
      print("check account mbut")
      try:
        driver.find_element(By.XPATH,  '//input[@type="password"][@aria-invalid="true"]')
        print("passwordnya salah cuk")
        driver.quit()
      except:
        try:
          driver.find_element(By.XPATH,  '//input[@id="phoneNumberId"]')
          print("OTP CUK")
          driver.quit()
        except:
          print("Wait redirected")

  driver.switch_to.window(main_page)
  driver.get('https://ayo.coca-cola.co.id/login/sat-coke-ayo-9-60')
  wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Google')]"))).click()
  for handle in driver.window_handles:
    if handle != main_page:
       login_page = handle
  driver.switch_to.window(login_page)

  try:
    time.sleep(3)
    driver.set_window_position(ind, 0)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-email="'+email+'"]'))).click()
    print("login ulang")
    driver.switch_to.window(main_page)
    try:
      wait.until(EC.url_to_be('https://ayo.coca-cola.co.id/c/sat-coke-ayo-9-60'))
      print("udah kelogin")
      wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@style,"background-color: rgb(0, 0, 0)")]//span[contains(text(),"Allow")]'))).click()
      wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@style,"background-color: rgb(0, 0, 0)")][contains(text(), "Klaim")]'))).click()

      status = False
      try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@style,"background-color: rgb(0, 0, 0)")]//span[contains(text(), "Redeem")]'))).click()
        try:
          driver.find_element(By.XPATH, '//p[@class="tap"][contains(text(), "Tap to expand")]').click()
          wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), " Show this barcode to the cashier")]'))).click()
          status = True
        except:
          try:
            driver.find_element(By.XPATH, '//span[@class="checkmark"][1]').click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@style,"background-color: rgb(0, 0, 0)")]//span[contains(text(), "Claim it")]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="tap"][contains(text(), "Tap to expand")]'))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), " Show this barcode to the cashier")]'))).click()
            status = True
          except:
            print("udah pernah claim mungkin akunnya")
        
        time.sleep(2)
        if(status==True):
          barcode = driver.find_element(By.XPATH, '//p[@class="barcode-value"]').text
          print(barcode)
          driver.find_element(By.XPATH, '//div[@class="flex-container"]').screenshot(barcode+".png")

      except:
        print("gagal klik redeem")
    except:
      print("gagal login")
  except:
    print("gagal relog")
  driver.close()
  print(user+" [done]")

jembut = []
totallist = int(len(empas))
for i in range(totallist):
  tut = totallist-thread
  jembut.append(empas[i])
  if len(jembut) == thread or i>=tut and i>0:
    counter = Counter()
    ind = 0
    for i in range(len(jembut)):
      t = threading.Thread(target=worker, args=(counter,ind,jembut[i]))
      t.start()
      ind+=300

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    jembut = []