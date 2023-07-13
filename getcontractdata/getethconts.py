from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tkinter import Tk


def init_auto(url):
    options= webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    options.add_argument('start-maximized')
    #options.add_argument('--headless')
    wd= webdriver.Chrome('chromedriver', options= options)
    wd.get(url)
    wd.find_element(By.XPATH, "//*[@id= 'btnCookie']").click()
    return wd

def get_contr(url):
    list_of_conts= []
    wd= init_auto(url)
    copy_buttons= wd.find_elements(By.XPATH, "//a[@class='js-clipboard btn btn-sm btn-icon btn-secondary me-1']")
    for k in copy_buttons:
        for s in range(2):
            try:
                #print(k.get_attribute('class'))
                action= ActionChains(wd)
                sub= WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='js-clipboard btn btn-sm btn-icon btn-secondary me-1']")))
                #copy_button.click()
                k.click()
                list_of_conts.append(Tk().clipboard_get())
            except:
                #print("Error")
                continue
    wd.close()
    return list_of_conts

def get_ethconts(address):
    url= 'https://etherscan.io/address/{}#code'.format(address)
    listconts= get_contr(url)
    return listconts

