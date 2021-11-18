from selenium import webdriver as wd
import time

# 아래 3개의 모듈을 한묶음으로 많이 사용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome 옵션 주기
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

chrome_options = Options()

# headless 모드
# chrome_options.add_argument('--headless') # 브라우저가 실행되지 않는 옵션

browser = wd.Chrome('./chromeDriver/chromedriver.exe', options=chrome_options)

browser.implicitly_wait(3)

browser.set_window_size(1024, 768)

browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용 확인하기
# print(f'first page contents : {browser.page_source}')

# //*[@id="dlMaker_simple"]/dd/div[2]/button[1]

# WebDriverWait(browser, 3) : browser가 3초간 기다림
# EC.presence_of_element_located : 요소가 자리 잡을 때 까지 
# By.XPATH : xpath에 의해 선택된 요소
# 3초 안에 로딩 되지 않으면 종료하고, 3초 전에 나오면 클릭할 거야!!!
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 원하는 상품 선택하기 //*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label'))).click()

# 2차 페이지 내용 확인하기
# print(f'second page contents : {browser.page_source}')

# 에러 방지(로딩 타임 주기)
time.sleep(2)

# BeautifulSoup 생성
bs = BeautifulSoup(browser.page_source, 'lxml')

# 소스코드 정리해서 보기
# print(bs.prettify())

prod_list = bs.select('div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer:not(.product-pot)')

print("맥북 리스트 : ", len(prod_list))

# 데이터 추출하기
for prod in prod_list:
    # 상품명, 이미지, 가격
    print(prod.select('p.prod_name > a')[0].text.strip())
    print(prod.select('a.thumb_link > img')[0]['src'])
    if len(prod.select('p.price_sect > a')) == 0:
        print("가격 비교 예정")
    else:        
        print(prod.select('p.price_sect > a')[0].text.strip())

browser.close()

















