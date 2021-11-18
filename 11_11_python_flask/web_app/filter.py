from web_app import app, datetime, time

@app.template_filter('datetime_format')
def datetime_format(value):
    if value is None:
        return ""

    # 클라이언트의 현재 시스템의 local 타임
    # 클라이언트의 local 타임을 datetime형식으로 만들어서 표현
    # 게시글을 보는 사람이 있는 지역의 시간(현재 컴퓨터의 시간)
    now_timestamp = time.time()
    # print("현재 로컬 타임 :", now_timestamp)

    # datetime 객체에 fromtimestamp, utcfromtimestamp 함수가 있다.

    # 클라이언트의 시간을 기준으로 datetime 객체를 만듦
    # print(datetime.fromtimestamp(now_timestamp))

    # utcfromstamp는 UTC datetime 을 반환
    # db에 저장된 UTC format과 같은 형태로 반환됨
    # print(datetime.utcfromtimestamp(now_timestamp))

    # 시간차 
    offset_time = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    # print("offset_time : ", offset_time)

    # db에 저장된 UTC 타임을 다시 현재의 로컬타임으로 변환해줌
    value = datetime.fromtimestamp((int(value) / 1000)) + offset_time

    # strftime() : format을 변경하는 함수
    return value.strftime('%Y-%m-%d %H:%M:%S')
