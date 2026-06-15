TEST_DESCRIPTION = '개인 회원 - 일반 로그인'
'''
개인 회원으로 일반 로그인 진행 테스트 스크립트입니다.
아래와 같은 절차로 진행됩니다
1. 홈페이지 진입
2. 로그인 버튼 클릭하여 로그인 페이지 진입
3. 로그인 시도
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import traceback
import time

LOGIN_LINK_SELECTOR = "#wrap > div.header-wrapper > div > div > div > div > div > div > div.header_top > div > ul > li:nth-child(5) > a"
EMAIL_INPUT_SELECTOR = "#wrap > div.layout__main--without-search > div > form > div:nth-child(2) > div > input"
PASSWORD_INPUT_SELECTOR = "#wrap > div.layout__main--without-search > div > form > div:nth-child(3) > div > input"
LOGIN_BUTTON_SELECTOR = "#wrap > div.layout__main--without-search > div > form > div.login-btn-box > button"


def start_driver(headless=False):
    options = Options()

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    # driver.maximize_window() 잘 안먹을때 추가

    return driver


def find_css(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def wait_class(driver, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, selector))
    )


def wait_css(driver, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )


driver = None

try:
    driver = start_driver()

    ### 1. 홈페이지 진입 ###

    driver.get('https://kream.co.kr')
    wait_class(driver, 'top_link')

    ### 2. 로그인 페이지 진입 ###

    find_css(driver, LOGIN_LINK_SELECTOR).click()
    wait_class(driver, 'input_item')

    ### 3. 일반 로그인 진행 ###

    email_id = find_css(driver, EMAIL_INPUT_SELECTOR)
    email_id.send_keys('')  # 테스트 id 입력 env파일로 빼서 넣기!

    pw = find_css(driver, PASSWORD_INPUT_SELECTOR)
    pw.send_keys('')  # 테스트 pw 입력 env파일로 빼서 넣기!

    loginbtn = find_css(driver, LOGIN_BUTTON_SELECTOR)
    loginbtn.click()

    time.sleep(1)

    ### 로그인 완료 ###
    wait_css(driver, '#wrap > div.header-wrapper > div > div > div > div > div > div > div.header_top > div > ul > li:nth-child(5) > a')

    logoutbtn = find_css(driver, '#wrap > div.header-wrapper > div > div > div > div > div > div > div.header_top > div > ul > li:nth-child(5) > a').text

    if logoutbtn == '로그아웃':
        pass
    else:
        raise Exception("로그인 후 로그아웃 버튼이 표시되지 않았습니다.")


except:
    print(traceback.format_exc())


finally:
    if driver:
        driver.quit()
