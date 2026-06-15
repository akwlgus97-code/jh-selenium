TEST_DESCRIPTION = '페이지 헬스체크'
'''
비회원으로 진행하는 테스트 스크립트입니다.
아래와 같은 절차로 진행됩니다
1. 사이트맵 진입
2. 헬스 체크 필요한 사이트 검수 (상태값 200, 랜딩 url 일치여부 확인)
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import traceback
import time
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def page_check(driver, element, pageurl):
    driver.find_element(By.XPATH, f'{element}').click()
    time.sleep(1)
    url = driver.current_url
    res = requests.get(url, timeout=10)
    if res.status_code == 200:
        if url == f'{pageurl}':
            driver.back()
        else:
            raise Exception
    else:
        raise Exception


def wait_xpath(driver, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, selector))
    )


driver = None

try:
    driver = start_driver()

    ### 1. 사이트맵 진입 ###
    driver.get('https://www.naver.com/more.html')
    wait_xpath(driver, '//*[@id="container"]/div[1]/ul/li[2]')

    ### 2. 상태 체크 원하는 메뉴 진입 ###
    page_check(driver, '//*[@id="container"]/div[1]/ul/li[2]/a', 'https://qcode.nid.naver.com/kr')
    page_check(driver, '//*[@id="container"]/div[1]/ul/li[3]/a', 'https://help.naver.com/index.help?lang=ko')
    page_check(driver, '//*[@id="container"]/div[1]/ul/li[4]/a', 'https://m.blog.naver.com/OfficialBlog.naver#menu_tab')
    page_check(driver, '//*[@id="container"]/div[1]/ul/li[5]/a', 'https://ko.dict.naver.com/#/main')


except:
    print(traceback.format_exc())


finally:
    if driver:
        driver.quit()
