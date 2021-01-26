from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import time
from datetime import datetime
import sys
import threading

dp = Tk()
main_frame = Frame(dp)
dp.geometry('500x500')
dp.title('Yes24 티켓팅 프로그램')
main_frame.pack()

driver = webdriver.Chrome("./es/chromedriver.exe")
driver2 = webdriver.Chrome("./es/chromedriver.exe")
wait = WebDriverWait(driver, 10)
wait2 = WebDriverWait(driver2, 10)
url = "https://www.yes24.com/Templates/FTLogin.aspx"


def url1():
    driver.get(url)
def url2():
    driver2.get(url)
def url_all():
    threading.Thread(target=url1).start()
    threading.Thread(target=url2).start()
url_all()

id_label = Label(main_frame, text = "첫번째 아이디")
id_label.grid(row = 1, column = 0)
id_entry = Entry(main_frame)
id_entry.grid(row = 1, column = 1)

pw_label = Label(main_frame, text = "첫번째 비밀번호")
pw_label.grid(row = 2, column = 0)
pw_entry = Entry(main_frame)
pw_entry.grid(row = 2, column =1)

id_label2 = Label(main_frame, text = "두번째 아이디")
id_label2.grid(row = 3, column = 0)
id_entry2 = Entry(main_frame)
id_entry2.grid(row = 3, column = 1)

pw_label2 = Label(main_frame, text = "두번째 비밀번호")
pw_label2.grid(row = 4, column = 0)
pw_entry2 = Entry(main_frame)
pw_entry2.grid(row = 4, column =1)

showcode_label = Label(main_frame, text = "공연번호")
showcode_label.grid(row=6, column = 0)
showcode_entry = Entry(main_frame)
showcode_entry.grid(row=6, column = 1)

date_label = Label(main_frame, text = "첫번째 날짜")
date_label.grid(row=7, column = 0)
date_entry = Entry(main_frame)
date_entry.grid(row=7, column = 1)

date_label2 = Label(main_frame, text = "두번째 날짜")
date_label2.grid(row=7, column = 2)
date_entry2 = Entry(main_frame)
date_entry2.grid(row=7, column = 3)

round_label = Label(main_frame, text = "첫번째 회차")
round_label.grid(row = 8, column = 0)
round_entry = Entry(main_frame)
round_entry.grid(row=8, column = 1)

round_label2 = Label(main_frame, text = "두번째 회차")
round_label2.grid(row = 8, column = 2)
round_entry2 = Entry(main_frame)
round_entry2.grid(row=8, column = 3)

ticket_label = Label(main_frame, text = "티켓 수")
ticket_label.grid(row = 9, column = 0)
ticket_entry = Entry(main_frame)
ticket_entry.grid(row=9, column = 1)

def login_go():
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[1]/input'))).send_keys(id_entry.get())
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[2]/input').send_keys(pw_entry.get())
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span/em').click()
def login_go2():
    wait2.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[1]/input'))).send_keys(id_entry2.get())
    driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[2]/input').send_keys(pw_entry2.get())
    driver2.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span/em').click()
def login_go3():
    threading.Thread(target=login_go).start()
    threading.Thread(target=login_go2).start()

def link_go():
    driver.switch_to_window(driver.window_handles[0])
    driver.execute_script("window.open('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=" + showcode_entry.get() + "');")
    driver.switch_to_window(driver.window_handles[-1])   
def link_go2():
    driver2.switch_to_window(driver2.window_handles[0])
    driver2.execute_script("window.open('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=" + showcode_entry.get() + "');")
    driver2.switch_to_window(driver2.window_handles[-1])  
def link_all():
    threading.Thread(target=link_go).start()
    threading.Thread(target=link_go2).start()

def seat_macro():
    driver.switch_to_default_content()
    frame = driver.find_element_by_name('ifrmSeatFrame')
    driver.switch_to.frame(frame)
    shot = 0
    while 1:
        try:
            driver.find_element_by_class_name('s9').click()
            shot = shot + 1
        except:
            try:
                driver.find_element_by_class_name('s6').click()
                shot = shot + 1
            except:
                try:
                    driver.find_element_by_class_name('s3').click()
                    shot = shot + 1
                except:
                    try:
                        driver.find_element_by_class_name('s4').click()
                        shot = shot + 1
                    except:
                        try:
                            driver.find_element_by_class_name('s5').click()
                            shot = shot + 1  
                        except:
                            try:
                                driver.find_element_by_class_name('s1').click()
                                shot = shot + 1
                            except:
                                try:
                                    driver.find_element_by_class_name('s7').click()
                                    shot = shot + 1
                                except:
                                    try:
                                        driver.find_element_by_class_name('s8').click()
                                        shot = shot + 1
                                    except:
                                        try:
                                            driver.find_element_by_class_name('s2').click()
                                            shot = shot + 1
                                        except:
                                            try:
                                                driver.find_element_by_class_name('s10').click()
                                                shot = shot + 1
                                            except:
                                                break
        if shot == int(ticket_entry.get()):
            break
    driver.find_element_by_css_selector('#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(2) > a').click()   
    driver.switch_to.default_content()
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[2]/a[2]').click()
def seat_macro2():
    driver2.switch_to_default_content()
    frame2 = driver2.find_element_by_name('ifrmSeatFrame')
    driver2.switch_to.frame(frame2)
    shot = 0
    while 1:
        try:
            driver2.find_element_by_class_name('s9').click()
            shot = shot + 1
        except:
            try:
                driver2.find_element_by_class_name('s6').click()
                shot = shot + 1
            except:
                try:
                    driver2.find_element_by_class_name('s3').click()
                    shot = shot + 1
                except:
                    try:
                        driver2.find_element_by_class_name('s4').click()
                        shot = shot + 1
                    except:
                        try:
                            driver2.find_element_by_class_name('s5').click()
                            shot = shot + 1  
                        except:
                            try:
                                driver2.find_element_by_class_name('s1').click()
                                shot = shot + 1
                            except:
                                try:
                                    driver2.find_element_by_class_name('s7').click()
                                    shot = shot + 1
                                except:
                                    try:
                                        driver2.find_element_by_class_name('s8').click()
                                        shot = shot + 1
                                    except:
                                        try:
                                            driver2.find_element_by_class_name('s2').click()
                                            shot = shot + 1
                                        except:
                                            try:
                                                driver2.find_element_by_class_name('s10').click()
                                                shot = shot + 1
                                            except:
                                                break
        if shot == int(ticket_entry.get()):
            break
    driver2.find_element_by_css_selector('#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(2) > a').click()   
    driver2.switch_to.default_content()
    driver2.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[2]/a[2]').click()
def seat_all():
    threading.Thread(target=seat_macro).start()
    threading.Thread(target=seat_macro2).start()

def go():
    #날짜
    driver.find_element_by_id(date_entry.get()).click()
    #회차
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul/li['+ round_entry.get() + ']'))).click()
    driver.switch_to_default_content()
    wait.until(EC.presence_of_all_elements_located((By.ID, 'ulTime')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[1]/a/img'))).click()  
def go2():
    #날짜
    driver2.find_element_by_id(date_entry2.get()).click()
    #회차
    wait2.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul/li['+ round_entry2.get() + ']'))).click()
    driver2.switch_to_default_content()
    wait2.until(EC.presence_of_all_elements_located((By.ID, 'ulTime')))
    wait2.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[1]/a/img'))).click()
def go_all():
    threading.Thread(target=go).start()
    threading.Thread(target=go2).start()

login_button = Button(main_frame, text = "로그인", command = login_go3, height = 2)
login_button.grid(row=4, column = 2)
link_button = Button(main_frame, text = "직링", command = link_all, height = 2)
link_button.grid(row=5, column = 1)
start_button = Button(main_frame, text = "날짜", command = go_all, height = 2)
start_button.grid(row=10, column = 1)
chair_button = Button(main_frame, text = "첫번째 좌석", command = seat_macro, height = 2)
chair_button.grid(row=11, column = 1)
chair_button2 = Button(main_frame, text = "두번째 좌석", command = seat_macro2, height = 2)
chair_button2.grid(row=11, column = 2)
chair_all = Button(main_frame, text = "좌석 일괄 시작", command = seat_all, height = 2)
chair_all.grid(row=12, column = 1)
dp.mainloop()
