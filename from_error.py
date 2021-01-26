def from_error():
    driver.find_element_by_xpath("/html/body/div[19]/div[11]/div/button").click()
    wait.until(EC.element_to_be_clickable((By.ID, "rdoDeliveryBase"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#StepCtrlBtn04 > a:nth-child(2)')))
    driver.find_element_by_css_selector('#StepCtrlBtn04 > a:nth-child(2)').click()
    #무통장
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rdoPays22'))).click()
    #신한
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#selBank > option:nth-child(5)'))).click()
    #동의 2개
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#cbxCancelFeeAgree'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#chkinfoAgree'))).click()
    #결제
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#StepCtrlBtn05 > a:nth-child(2)')))