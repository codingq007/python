import requests
from lxml.html import fromstring, tostring


def main():
    session = requests.Session()

    # 스크래핑 대상 URL을 지정
    response = session.get('http://www.naver.com')

    urls = scrape_news(response)

    for name, url in urls.items():
        print(name, url)

def scrape_news(response):

    # 딕셔너리 선언
    urls = {}

    root = fromstring(response.content)

    # root.make_links_absolute(response.url)


    for a in root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]/div[@class="popup_wrap"]/a[@class="btn_popup"]'):
        # a 문자열 출력
        print(tostring(a))

        # 언론사명, 언론사 링크 주소
        name, url = extract_contents(a)

        urls[name] = url
    return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.get('href')

    # dom.xpath('../../a[@class="thumb"]/img')의 값은 리스트이다.

    img_list = dom.xpath('../../a[@class="thumb"]/img')
    name = img_list[0].get('alt')

    # 위의 코드를 줄여서 아래와 같이 작성
    # name = dom.xpath('../../a[@class="thumb"]/img')[0].get('alt')

    return name, link

if __name__ == '__main__':
    main()    







