# pip install pymongo

import pymongo

mem = {
    "이름" : "임꺽정",
    "나이" : 30,
    "거주지" : "대전",
    "키" : 180,
    "몸무게" : 78,
    "사진" : ["a.jpg", "b.jpg"]
}

mem2 = {
    "이름" : "고길동",
    "나이" : 34,
    "거주지" : "광주",
    "몸무게" : 78,
    "학교" : "우리대",
    "사진" : ["c.jpg", "d.jpg"]
}

# MongoClient: 접속해주는 라이브러리(주소, 포트를 넣어준면 connection 객체를 리턴)
conn = pymongo.MongoClient("localhost", 27017)

# test라는 데이터베이스가 없으면 새로생성, 있으면 넘어감
# db는 test 데이터베이스
db = conn.test


# members라는 컬렉션을 만든다.
# members 컬렉션이 있으면 그대로 가져오고, 없으면 새로 생성
collection = db.members

# 데이터 삽입
# collection.insert(mem)

# collection.insert_one(mem2)

# 데이터 검색
# cursor 객체가 리턴됨.
# results = collection.find()

# <pymongo.cursor.Cursor object at 0x0000027548D7D730>
# print(results)

# results = collection.find({"학교":"우리대"})
# results = collection.find({"이름": "고길동", "학교":"우리대"}) # and 연산됨

# or 연산
# results = collection.find({"$or":[{"이름": "고길동"}, {"학교":"우리대"}]}) 
# results = collection.find({"$or":[{"이름": "고길동"}, {"학교":"우리대"}, {"이름":"홍길동"}]}) 

# 첫번째 조회된 것 하나만 가져온다.
# result = collection.find_one({"이름" : "홍길동"})
# print(result)

# results = collection.find({"나이" : {"$gt" : 30}}) # 나이 > 30 greater than
# results = collection.find({"나이" : {"$gte" : 30}}) # 나이 >= 30
# results = collection.find({"나이" : {"$gt" : 30, "$lt": 50}}) # 30 < 나이 < 50

# 원하는 필드만 조회하기
# results = collection.find({"나이" : {"$gt" : 30, "$lt": 50}}, {"이름": True}) # 이름 필드만 출력 + id 추가 출력
# results = collection.find({"나이" : {"$gt" : 30, "$lt": 50}}, {"_id":False, "이름": True}) # 이름 필드만 출력

## 이름 필드와 거주지 필드만 출력(id 생략)
# results = collection.find({"나이" : {"$gt" : 30, "$lt": 50}}, {"_id":False, "이름": True, "거주지": True})
# ## 5개만 출력
# results = collection.find({"나이" : {"$gt" : 30, "$lt": 50}}, {"_id":False, "이름": True, "거주지": True}).limit(5)

# results = collection.find({"나이" : {"$gt" : 20, "$lt": 50}}, {"_id":False, "이름": True, "거주지": True}).limit(5)
results = collection.find({"나이" : {"$gt" : 20, "$lt": 50}}, {"_id":False, "이름": True, "거주지": True}).skip(3).limit(5)

# 전체 데이터 가져오기
# results = collection.find({})

# sort: 1이면 오름차순, -1이면 내림차순
results = collection.find({"나이" : {"$gt" : 20, "$lt": 50}}, {"_id":False, "이름": True, "거주지": True}).sort("이름", -1).skip(3).limit(5)


for r in results:
    print(r)

