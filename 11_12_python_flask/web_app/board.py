from os import name
from web_app import *
from flask import jsonify

bp = Blueprint("board", __name__, url_prefix="/board")

# 첨부파일 삭제 함수
def board_del_attachfile(filename):
    abs_path = os.path.join(app.config["BOARD_ATTACH_FILE_PATH"], filename)
    if os.path.exists(abs_path):
        os.remove(abs_path)
        return True
    return False

@bp.route("/ajax")
def ajaxtest():
    return render_template("ajax_test.html")

@bp.route("/test")
def test():
    return "AJAX TEST"    


@bp.route("/upload_image", methods=["POST"])
# @app.route("/board/a/upload_image", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # image라는 이름으로 저장된 file을 가져옴.
        file = request.files["image"]
        
        # file이 유효하고 확장자도 허용가능한 확장자이면
        if file and allowed_file(file.filename):
            # 랜덤한 8자리 파일명으로 파일이 생성
            filename = "{}.jpg".format(rand_generator())

            # file명과 결합된 실제파일 경로
            savepath = os.path.join(app.config["BOARD_IMAGE_PATH"], filename)

            # 서버에 파일을 저장
            file.save(savepath)
            return url_for("board.board_images", filename=filename)

# 이미지가 저장된 디렉토리에 접근하기 위해서 send_from_directory함수를 사용한다.
@bp.route("/images/<filename>")
def board_images(filename):
    return send_from_directory(app.config["BOARD_IMAGE_PATH"], filename)

@bp.route("/files/<filename>")
def board_files(filename):
    return send_from_directory(app.config["BOARD_ATTACH_FILE_PATH"], filename, as_attachment=True)    

######################## list ########################
# @app.route("/list")
@bp.route("/list")
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

    return render_template("bbs/list.html", docs = docs,
                                        page = page,
                                        limit = limit,
                                        block_start = block_start,
                                        block_last = block_last,
                                        last_page_num = last_page_num,
                                        search = search,
                                        keyword = keyword,
                                        title="리스트")


######################## view ########################
# clean url, fancy url 표기법(사용편의성, 보안적인 측면고려)
@bp.route('/view/<idx>')
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
                "writer_id":data.get("writer_id", ""),
                "attachfile": data.get("attachfile", "")
            }

            # comment 컬렉션에서 root_id에 해당하는 댓글 가져온다.
            # comment = mongo.db.comment
            # comments = comment.find({"root_id": str(data.get("_id"))})

            return render_template("bbs/view.html", 
                    result = result, 
                    # comments = comments, # 댓글을 view에 넘겨준다.
                    page=page, 
                    search=search, 
                    keyword=keyword,
                    title = "글보기")
    return abort(404) # 오류 출력


######################## write ########################
# methods 지정하지 않으면 GET방식
@bp.route('/write', methods=["GET", "POST"])
@login_required # 로그인을 하지 않은 사용자의 접근을 제한하기 위한 데코레이터
def board_write():
    # if session.get("id") is None:
    #     return redirect(url_for("member_login"))

    if request.method == "POST":

        filename = None

        # 첨부 파일이 있는지 확인
        if "attachfile" in request.files:
            # 첨부파일이 있으면 해당 파일을 받아온다.
            file = request.files["attachfile"]

            # 파일의 이름이 허용가능한 파일인지 확인
            if file and allowed_file(file.filename):
                # 악성 파일인지 체크 후에 새로운 파일명을 얻어온다.
                filename = check_filename(file.filename)
                # 새로운 파일명과 조인을 해서 저장
                file.save(os.path.join(app.config["BOARD_ATTACH_FILE_PATH"], filename))


        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        # print(name, title, contents)

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
            "hit": 0,            
        }

        if filename is not None:
            post_data["attachfile"] = filename

        doc = board.insert_one(post_data)
        # return str(doc.inserted_id)
        return redirect(url_for("board.board_view", idx=doc.inserted_id))
    else:
        return render_template("bbs/write.html", title = "글쓰기")

##################### modify ###################
@bp.route("/modify/<idx>", methods=["GET", "POST"])
def modify(idx):
    if request.method == "GET":
        board = mongo.db.board
        doc = board.find_one({"_id":ObjectId(idx)})

        if doc is None:
            flash("게시물이 존재하지 않습니다!!")
            return redirect(url_for("board.lists"))
        else:
            if session.get("id") == doc.get("writer_id"):
                return render_template("bbs/modify.html", doc=doc, title="글수정")
            else:
                flash("글수정 권한이없습니다.")
                return render_template("bbs/modify.html", doc=doc, title="글수정")

    else:
        title = request.form.get("title")
        contents = request.form.get("contents")

        deloldfile = request.form.get("oldfile", "")

        print("---------------")
        print("deloldfile :", deloldfile)
        print("---------------")


        board = mongo.db.board
        doc = board.find_one({"_id": ObjectId(idx)})

        if session.get("id") == doc.get("writer_id"):
            filename = None
            # 첨부파일이 추가된 경우
            print("파일추가 없이 수정클릭 !!!!! : ",request.files["attachfile"])
            print("파일추가 없이 수정클릭 !!!!! : ",request.files)
            print("파일추가 없이 수정클릭 !!!!! : ",type(request.files))


            if request.files["attachfile"]: # 파일을 첨부하면
            # if "attachfile" in request.files:
                file = request.files['attachfile']
                print("file : ", file)

                if file and allowed_file(file.filename):
                    filename = check_filename(file.filename)
                    # 새로운 파일 저장
                    file.save(os.path.join(app.config["BOARD_ATTACH_FILE_PATH"], filename))

                    # 데이터베이스에 있는 첨부파일(이전 파일)
                    if doc.get("attachfile"):
                        board_del_attachfile(doc.get("attachfile"))

            else: # 첨부파일을 추가하지 않은 경우
                # 체크박스가 체크가되면 문자열로 "on"값이 들어온다.
                if deloldfile == "on":
                    filename = None
                    if doc.get("attachfile"): # 데이터베이스에 있는지 체크
                        board_del_attachfile(doc.get("attachfile"))
                else: # 체크박스가 체크되지 않았을 경우                        
                    filename = doc.get("attachfile") # 이전 파일이름으로 설정
                    print("DB에 있는 파일 : ", filename)


            board.update_one({"_id": ObjectId(idx)},{
                "$set":{
                    "title":title,
                    "contents": contents,
                    "attachfile" : filename
                }
            })

            flash("수정 완료 되었습니다!!")
            return redirect(url_for("board.board_view", idx = idx))
        else:
            flash("글수정 권한이 없습니다.")
            return redirect(url_for("board.lists"))

##################### delete ###################
@bp.route("/delete/<idx>", methods=["GET", "POST"])
def delete(idx):
    board = mongo.db.board
    doc = board.find_one({"_id":ObjectId(idx)})
    
    if doc.get("writer_id") == session.get("id"):
        board.delete_one({"_id":ObjectId(idx)})
        flash("삭제 완료 되었습니다!!")
    else:
        flash("삭제 권한이 없습니다!!")

    return redirect(url_for("board.lists"))

##################### 댓글 저장하기 ###################
@bp.route("/comment_write", methods=["POST"])
@login_required
def comment_write():
    if request.method == "POST":
        name = session.get("name")
        writer_id = session.get("id")
        root_id = request.form.get("root_id")
        comment = request.form.get("comment")
        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        collection_comment = mongo.db.comment

        post_data = {
            "root_id":str(root_id),
            "writer_id": writer_id,
            "name": name,
            "comment": comment,
            "regdate": current_utc_time
        }

        collection_comment.insert_one(post_data)
        return redirect(url_for("board.board_view", idx=root_id))

##################### 댓글 목록 ###################
@bp.route("/comment_list/<root_id>", methods=["GET"])

def comment_list(root_id):
    comment = mongo.db.comment

    # 게시글의 id와 같은 댓글을 모두 가져오기(실제 데이터가 comments에 저장되는 것은 아니다.)
    # collection.find({})의 리턴값은 pymongo.cursor.Cursor
    comments = comment.find({"root_id": str(root_id)}).sort("regdate", -1)

    # 실제 데이터를 가져올 때는 해당 Cursor를 가지고 html에서 rendering 할 때

    # ajax로 데이터를 처리할 때는 json 형태로 처리해야 하기 때문에..
    # Cursor를 받아서 처리할 수 없다. 따라서, 딕셔너리로 변환해서 넘겨줘야 한다.
    comment_list = []
    
    for comment in comments:
        comment_list.append({
            "id" : str(comment.get("_id")),
            "root_id": comment.get("root_id"),
            "name": comment.get("name"),
            "writer_id": comment.get("writer_id"),
            "comment": comment.get("comment"),
            # html에서는 jinja를 이용해서 날짜포맷을 변환 했지만,
            # ajax에서는 javascript로 변환해서 처리해야 한다.
            # 따라서, 변환해서 넘겨준다.
            "regdate": datetime_format(comment.get("regdate"))
        })

    # jsonify(키=값, 키=값...) json형태로 만든다.
    return jsonify(key="success", lists=comment_list)            
    


