
from time import sleep
from selenium import webdriver
import login
import selenium
import time

def logg():
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(login.usernae)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(login.password)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

def noti():
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

def likes():

    browser.get('https://www.instagram.com/explore/tags/mumbai/?hl=en')
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
    for i in range(2):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()




browser = webdriver.Chrome('C:/Users/Huzefa/Downloads/chromedriver_win32/chromedriver.exe')

browser.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(2)
logg()
time.sleep(2)
noti()
time.sleep(2)
likes()


