from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui as pag
from PIL import ImageGrab
from tkinter import *
import time

R_cc = (0, 204, 204)
f1_start = (26, 265)
f1_end = (636, 678)

dp = Tk()
main_frame = Frame(dp)
main_frame.pack()

driver = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(driver, 15)

url = "https://ticket.yes24.com/Pages/Login/LoginEnt.aspx?ReturnURL="
driver.get(url)

dp.mainloop()