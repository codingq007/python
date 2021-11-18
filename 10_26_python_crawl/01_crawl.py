# 파이썬은 파일 오픈시에 cp949(ansi) 형식으로 읽어 들인다.
# utf8로 인코딩이 되어 있다는 것을 알려줘야 한다.
fp = open('utf-8.txt', 'r', encoding='utf8')
print(fp.read())
fp.close()

fp = open('utf-8.txt', 'rb')
print(fp.read().decode('utf8'))
fp.close()