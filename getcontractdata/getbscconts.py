from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tkinter import Tk

def get_bsc_scan(address):
    list_conts= []
    url= 'https://bscscan.com/address/{}#code'.format(address)
    options= webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    options.add_argument('start-maximized')
    options.add_argument("--disable-gpu")
    wd= webdriver.Chrome('chromedriver', options= options)
    wd.get(url)
    wd.find_element(By.XPATH, "//*[@id= 'btnCookie']").click()
    copy_buttons= wd.find_elements(By.XPATH, "//a[@class='js-clipboard btn btn-sm btn-icon btn-secondary mr-1']")
    for k in copy_buttons:
        action= ActionChains(wd)
        sub= WebDriverWait(wd, 19).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='js-clipboard btn btn-sm btn-icon btn-secondary mr-1']")))
        k.click()
        list_conts.append(Tk().clipboard_get())
    return list_conts
    
get_bsc_scan('0x74f08aF7528Ffb751e3A435ddD779b5C4565e684')