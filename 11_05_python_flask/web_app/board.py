from web_app import *

######################## list ########################
@app.route("/list")
def lists():
    # 페이지 값(값이 없는 경우에는 기본값을 1로하고, 그 자료형은 int형)
    page = request.args.get("page", default=1, type=int)

    # 한페이지당 몇개의 게시물을 출력할지를 지정(보통 고정해서 사용하는 경우도 많음)
    limit = request.args.get("limit", 6, type=int)

    ### 검색 처리
    search = request.args.get("search", -1, type=int)
    keyword = request.args.get("keyword", "", type=str)

    # 최종 완성된 쿼리를 만드는 변수
    query = {}

    search_list = []

    # $regex => SQL의 like 연산자 기능, 검색어 '길' => 홍길동, 고길동, 고영길....
    # 검색 대상을 지정
    if search == 0:
        search_list.append({"title":{"$regex": keyword}})
    elif search == 1:
        search_list.append({"contents":{"$regex": keyword}})
        
    elif search == 2:
        search_list.append({"title":{"$regex": keyword}})
        search_list.append({"contents":{"$regex": keyword}})
        
    elif search == 3:
        search_list.append({"name":{"$regex": keyword}})

    
    # 검색대상이 한개라도 존재할 경우 query 변수에 $or 연산자 이용한다.    
    if len(search_list) > 0:
        query = {"$or": search_list}

    '''
        검색의 일괄 처리
        { "$or" :[
            {"title":{"$regex":"자바"}},
            {"contents":{"$regex":"C언어"}},
            {"name":{"$regex":"C++"}}
        ]}

        { "$and" :[
            {"title":{"$regex":"자바"}},
            {"contents":{"$regex":"C언어"}},
            {"name":{"$regex":"C++"}}
        ]}

    '''
    print(query)
    print("================")

    board = mongo.db.board
    # 현재 페이지가 2페이지이면 (2-1)*10은 건너띄고, 10개만 표시 limit(10)
    # docs = board.find(query).skip((page-1) * limit).limit(limit)
    docs = board.find(query).skip((page-1) * limit).limit(limit).sort("regdate", -1)

    ## 전체 게시물의 개수
    total_cnt = board.find(query).count()

    ## 마지막 페이지 수
    last_page_num = math.ceil(total_cnt/limit)

    # 한블럭에 보여줄 페이지 수
    block_size = 5

    # 현재 페이지의 블럭 위치 계산하기(0, 1, 2, ...)
    block_num = int((page - 1) /block_size)

    # 블럭의 시작값 : 첫번째 블럭 시작값 1, 두번째 블럭 시작값 6
    block_start = int((block_size * block_num) + 1)

    # 블럭의 마지막값 : 첫번째 블럭의 마지막 값 5, 두번째 ~ : 10
    # 첫번째 블럭의 마지막 값: 1 + 4, 두번째 블럭의 마지막 값 : 6 + 4
    block_last = block_start + (block_size - 1)

    # return render_template("list.html", docs = docs)

    return render_template("list.html", docs = docs,
                                        page = page,
                                        limit = limit,
                                        block_start = block_start,
                                        block_last = block_last,
                                        last_page_num = last_page_num,
                                        search = search,
                                        keyword = keyword)


######################## view ########################
# clean url, fancy url 표기법(사용편의성, 보안적인 측면고려)
@app.route('/view/<idx>')
@login_required
def board_view(idx):        
# @app.route('/view')
# def board_view():
    # idx = request.args.get("idx")
    if idx is not None:
        # get방식으로 전달되는 값을 받아오기
        page = request.args.get("page")
        search = request.args.get("search")
        keyword = request.args.get("keyword")

        board = mongo.db.board

        # 게시물은 하나 따라서, find_one, idx를 ObjectId로 변환
        # data = board.find_one({"_id":ObjectId(idx)})

        # return_document가 True이면 조회수가 업데이트된 후에 변수에 넘기겠다는 의미
        data= board.find_one_and_update({"_id":ObjectId(idx)}, {"$inc":{"hit":1}}, return_document=False)

        if data is not None:
            result = {
                "id": data.get("_id"),
                "name": data.get("name"),
                "title": data.get("title"),
                "contents":data.get("contents"),
                "regdate" : data.get("regdate"),
                "hit" : data.get("hit"),
                "writer_id":data.get("writer_id", "")
            }

            return render_template("view.html", result = result, page=page, search=search, keyword=keyword)
    return abort(404) # 오류 출력


######################## write ########################
# methods 지정하지 않으면 GET방식
@app.route('/write', methods=["GET", "POST"])
@login_required # 로그인을 하지 않은 사용자의 접근을 제한하기 위한 데코레이터
def board_write():
    # if session.get("id") is None:
    #     return redirect(url_for("member_login"))

    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        print(name, title, contents)

        # utc는 국제 표준시(GMT(Greenwich Mean Time)) : UTC, GMT 혼용하여 사용한다.
        # UTC, GMT는 시간차가 거의 없음.

        # 데이터베이스에 시간을 저장할 때는 가장 가공하기 쉬운
        # 형태로 저장을 해놓아야 한다.  
        # 재가공하기 쉬운 형태가 바로 timestamp이다.

        # utc time은 1000분의 1초로 표현        
        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        # 컬렉션 생성
        board = mongo.db.board

        post_data = {
            "name": name,
            "title": title,
            "contents":contents,
            "regdate" : current_utc_time,
            # 글수정, 삭제시 본인이 쓴글인지 확인하기 위한 용도
            # unique한 값을 이용하기 위해 id, email을 생각할 수 있으나
            # email은 회원정보 수정시..바뀔 수 있다.
            # 바뀌지 않는 값을 사용하는 것이 본인을 확실하게 확인할 수 있다.
            "writer_id" : session.get("id"),
            "hit": 0
        }

        doc = board.insert_one(post_data)
        # return str(doc.inserted_id)
        return redirect(url_for("board_view", idx=doc.inserted_id))
    else:
        return render_template("write.html")

##################### modify ###################
@app.route("/modify/<idx>", methods=["GET", "POST"])
def modify(idx):
    if request.method == "GET":
        board = mongo.db.board
        doc = board.find_one({"_id":ObjectId(idx)})

        if doc is None:
            flash("게시물이 존재하지 않습니다!!")
            return redirect(url_for("lists"))
        else:
            if session.get("id") == doc.get("writer_id"):
                return render_template("modify.html", doc=doc)
            else:
                flash("글수정 권한이없습니다.")
                return render_template("modify.html", doc=doc)

    else:
        title = request.form.get("title")
        contents = request.form.get("contents")

        board = mongo.db.board
        doc = board.find_one({"_id": ObjectId(idx)})

        if session.get("id") == doc.get("writer_id"):
            board.update_one({"_id": ObjectId(idx)},{
                "$set":{
                    "title":title,
                    "contents": contents
                }
            })
            flash("수정 완료 되었습니다!!")
            return redirect(url_for("board_view", idx = idx))
        else:
            flash("글수정 권한이 없습니다.")
            return redirect(url_for("lists"))

##################### delete ###################
@app.route("/delete/<idx>", methods=["GET", "POST"])
def delete(idx):
    board = mongo.db.board
    doc = board.find_one({"_id":ObjectId(idx)})
    
    if doc.get("writer_id") == session.get("id"):
        board.delete_one({"_id":ObjectId(idx)})
        flash("삭제 완료 되었습니다!!")
    else:
        flash("삭제 권한이 없습니다!!")

    return redirect(url_for("lists"))
