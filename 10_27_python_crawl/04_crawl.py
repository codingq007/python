import requests
import lxml.html

def main():

    # 스크랩핑 대상 URL 지정
    response = requests.get('https://www.naver.com/')

    urls, press_names = scrape_news(response)

    # for url in urls:
    #     print(url)

    for i in range(len(urls)):    
        print(press_names[i]+"\t: ", urls[i])   

def scrape_news(response):

    urls =[] 
    press_names = []


    print(response.content) # 디코딩 처리 안됨   
    print("============================")
    print(response.text) # 디코딩 처리 됨
    print("============================")

    # html 문서 내의 요소를 탐색할 수 있도록 문서 계층 구조로 생성
    root = lxml.html.fromstring(response.content)
    print("root : ", root)

    

    for img in root.cssselect('._NM_NEWSSTAND_THUMB>a.thumb>img'):
        # 언론사 이름
        press_name = img.get('alt')

        # 리스트 삽입
        press_names.append(press_name)


    # for a in root.cssselect('._NM_NEWSSTAND_THUMB .popup_wrap a.btn_popup'):
    for a in root.cssselect('._NM_NEWSSTAND_THUMB .popup_wrap a:nth-child(3)'):

        # 링크 주소 얻어오기
        url = a.get('href')

        # 링크 주소 리스트에 저장
        urls.append(url)

    return urls, press_names

if __name__ == '__main__':
    main()    


