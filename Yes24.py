from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import time, pyotp
from datetime import datetime

dp = Tk()
main_frame = Frame(dp)
dp.geometry('500x500')
dp.title('Yes24 티켓팅 프로그램')
main_frame.pack()

driver = webdriver.Chrome("es/chromedriver")
wait = WebDriverWait(driver, 30)
url = "https://www.yes24.com/Templates/FTLogin.aspx"
driver.get(url)

id_label = Label(main_frame, text="아이디")
id_label.grid(row=1, column=0)
id_entry = Entry(main_frame)
id_entry.grid(row=1, column=1)

pw_label = Label(main_frame, text="비밀번호")
pw_label.grid(row=2, column=0)
pw_entry = Entry(main_frame)
pw_entry.grid(row=2, column=1)

showcode_label = Label(main_frame, text="공연번호")
showcode_label.grid(row=4, column=0)
showcode_entry = Entry(main_frame)
showcode_entry.grid(row=4, column=1)

date_label = Label(main_frame, text="날짜")
date_label.grid(row=5, column=0)
date_entry = Entry(main_frame)
date_entry.grid(row=5, column=1)

round_label = Label(main_frame, text="회차")
round_label.grid(row=6, column=0)
round_entry = Entry(main_frame)
round_entry.grid(row=6, column=1)

ticket_label = Label(main_frame, text="티켓 수")
ticket_label.grid(row=7, column=0)
ticket_entry = Entry(main_frame)
ticket_entry.grid(row=7, column=1)


def login_go():
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[1]/input'))).send_keys(id_entry.get())
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/span[2]/input').send_keys(
        pw_entry.get())
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span/em').click()


def link_go():
    driver.switch_to_window(driver.window_handles[0])
    driver.execute_script(
        "window.open('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=" + showcode_entry.get() + "');")
    driver.switch_to_window(driver.window_handles[-1])


def seat_macro():
    try:
        driver.switch_to_default_content()
        frame = driver.find_element_by_name('ifrmSeatFrame')
        driver.switch_to.frame(frame)
        shot = 0
        while 1:
            try:
                driver.find_element_by_class_name('s1').click()
                shot = shot + 1
            except:
                try:
                    driver.find_element_by_class_name('s9').click()
                    shot = shot + 1
                except:
                    try:
                        driver.find_element_by_class_name('s6').click()
                        shot = shot + 1
                    except:
                        try:
                            driver.find_element_by_class_name('s4').click()
                            shot = shot + 1
                        except:
                            try:
                                driver.find_element_by_class_name('s3').click()
                                shot = shot + 1
                            except:
                                try:
                                    driver.find_element_by_class_name('s5').click()
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
        driver.find_element_by_css_selector(
            '#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(2) > a').click()
        driver.switch_to.default_content()
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[2]/a[2]').click()
    except:
        pass


def go():
    try:
        # 날짜
        driver.find_element_by_id(date_entry.get()).click()
        # 회차
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul/li[' + round_entry.get() + ']'))).click()
        driver.switch_to_default_content()
        wait.until(EC.presence_of_all_elements_located((By.ID, 'ulTime')))
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[6]/div[1]/div[3]/div/div[4]/div/div[1]/a/img'))).click()
    except:
        pass


def bank():
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rdoPays22"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selBank > option:nth-child(5)"))).click()
    driver.find_element_by_css_selector("#cbxCancelFeeAgree").click()
    driver.find_element_by_css_selector("#chkinfoAgree").click()
    driver.find_element_by_css_selector("#StepCtrlBtn05 > a:nth-child(2)").click()


def clock_time():
    clock = datetime.now().strftime('%H:%M:%S:%f')
    time_label.config(text=clock)
    time_label.after(1, clock_time)


login_button = Button(main_frame, text="로그인", command=login_go, height=2)
login_button.grid(row=2, column=3)
link_button = Button(main_frame, text="직링", command=link_go, height=2)
link_button.grid(row=3, column=1)
start_button = Button(main_frame, text="날짜 선택", command=go, height=2)
start_button.grid(row=8, column=1)
start2_button = Button(main_frame, text="좌석 선택", command=seat_macro, height=2)
start2_button.grid(row=9, column=1)
bank_button = Button(main_frame, text="무통장 결제", command=bank, height=2)
bank_button.grid(row=10, column=1)
time_label = Label(main_frame, height=2)
time_label.grid(row=11, column=1)
clock_time()

dp.mainloop()
