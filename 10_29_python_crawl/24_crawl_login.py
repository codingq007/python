import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Login 추가 정보
login_add_info = {
    'redirectUrl': 'http://www.danawa.com/member/myPage.php',
    'loginMemberType': 'general',
    'id': 'codingq',
    'isSaveId': 'true',
    'password': 'test007*'
}

# Headers 정보
headers = {
    'User-Agent' : UserAgent().chrome,
    'Referer': 'https://auth.danawa.com/login?url=http://www.danawa.com/member/myPage.php'
}

with req.session() as sess:
    # 로그인
    res = sess.post('https://auth.danawa.com/login', login_add_info, headers=headers)

    # if res.status_code !=200:
    #     raise Exception('Login failed')

    # print(res.content.decode('utf-8'))

    # 로그인 성공 후 페이지 이동
    res = sess.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

    # print(res.text)

    # bs4 생성
    soup = BeautifulSoup(res.text, 'lxml')

    chk_name = soup.find('p', class_="user")
    # print(chk_name)

    if chk_name is None:
        raise Exception('login failed. Wrong Password!!!')

    my_info = soup.select("div.my_info > div.sub_info > ul.info_list > li")

    print(my_info)

    print()
    
    # 로그인 후의 정보 출력하기
    print('=========== 나의 배송/주문 정보 ============ ')
    
    for info in my_info:
        title, value = info.find('span').string.strip(), info.find('strong').string.strip()

        # 출력
        print(f'{title} : {value}')