import pymongo
from pymongo import collection

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test
collection = db.members

mem3 = {
    "이름" : "장길산",
    "나이" : 65,
    "거주지" : "서울",
    "몸무게" : 100,
    "학교" : "마이대",
    "사진" : ["a.jpg", "bbb.jpg"]
}

# collection.insert(mem3)

################ update 처리 ################
# rs = collection.find({"이름":"장길산"})

# 주의 : 이경우에는 이름 필드외에 나머지 필드는 모두 지워짐.
# collection.update({"이름":"장길산"}, {"이름":"이황"})

# 여러개의 document(row)가 있더라도 하나의 document만 수정한다. 
# 여러개의 document를 수정하려면 multi=True, default로 multi = False로 설정
# collection.update({"이름":"장길산"}, {"$set": {"이름":"이황"}})

# 임꺽정을 모두 장길산으로 수정
# collection.update({"이름":"임꺽정"}, {"$set": {"이름":"장길산"}}, multi=True)

# 별명 필드 추가시 임꺽정이 없으면 수정되지 않는다.
# collection.update({"이름":"임꺽정"}, {"$set": {"별명":"이황짱"}})

# collection.update({"이름":"이황"}, {"$set": {"별명":"이황짱"}})

# 업데이트 대상이 존재하지 않으면 삽입, 존재하는 경우는 수정하라는 옵션 upsert = True : (update + insert)
# collection.update({"이름":"김연아"}, {"$set": {"별명":"연아짱"}}, upsert=True)

# 연산자 inc : 몸무게 필드 추가
collection.update({"이름":"이황"}, {"$inc":{"몸무게": 65}})


################ 삭제 처리 ################

# collection.remove({"이름": "장길산"}) # 장길산 모두 삭제

# collection.remove({}) # 모든 데이터가 삭제됨. 잘못쓰면 망함.

# delete_one, delete_many

# collection.delete_one({"이름":"고길동"}) # 첫번째 고길동만 삭제
collection.delete_many({"이름":"고길동"}) # 고길동 모두 삭제


rs = collection.find({})


for r in rs:
    print(r)


