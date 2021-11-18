# pip install selenium


import time
from selenium import webdriver as wd

# webdriver 설정
browser = wd.Chrome('./chromeDriver/chromedriver.exe')

# 브라우저 대기: 관행적으로 대기
browser.implicitly_wait(2)

# 브라우저 사이즈 조정
browser.set_window_size(1024, 768)

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용 가져오기
print(f'page contents :  {browser.page_source}')

# session ID
print(f'Session ID : {browser.session_id}')

# 타이틀 출력
print(f'Title : {browser.title}')

# 현재 URL 출력
print(f'URL : {browser.current_url}')

# 쿠키 정보 확인
print(f'URL : {browser.get_cookies()}')

# 검색어 input 가져오기
input_element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력하기
input_element.send_keys('손흥민')

# 검색어 전송(submit)
input_element.submit()

# 스크린 샷 저장 : 중간 중간 확인시에  필요
browser.save_screenshot('./website_01.jpg')

# time.sleep(3)
# browser.quit()
browser.close()