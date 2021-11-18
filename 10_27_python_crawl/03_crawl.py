from urllib import response
import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["C:/m-study/python_crawling/dn/test.jpg", "C:/m-study/python_crawling/dn/index.html"]

# 다운로드 리소스 URL
target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA5MjlfMTc2%2FMDAxNjMyODczNTc0Mjc2.A0zu1gSMwVh8O6Fmm9Io7gC0LXPIv7-rFwYjkuMCxtQg.jlqc8KGA9-Ufyzk86I9i1njb335eWb0p6Op-UYTsWp4g.JPEG.pupuhz%2FIMG_1817.JPG&type=a340", "http://google.com"
]

for i, url in enumerate(target_url):
    
    try:
        # response는 해당 url의 모든 정보를 갖고 있음.
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print('-------------------------------------')
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('-------------------------------------')

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    # HTTP 에러 발생시
    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    # URL 에러 발생시
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ", e.reason)
    # 성공
    else:
        print()
        print("Download Success!!")
