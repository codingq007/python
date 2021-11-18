import json
import requests

sess = requests.Session()

res = sess.get('http://httpbin.org/stream/20')

# 수신 확인
print(res.text)

# 
print(f"Encoding : {res.encoding}")

for line in res.iter_lines(decode_unicode=True):
    # Json으로 변환
    d = json.loads(line)

    for k, v in d.items():
        if(k != "headers"):            
            print(f"Key: {k}, Value: {v}")
        else:
            print("headers : ")
            for hk, hv in v.items():
                print(f"   key : {hk}, values: {hv}")

                

sess.close()        




