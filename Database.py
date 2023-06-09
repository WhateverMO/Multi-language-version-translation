import json
import os
import time

import pytz as pytz
import chardet
from db_struct import *

user_id_pool_size = 400
user_id_pool_lock_size = 200
author_id_pool_size = 400
author_id_pool_lock_size = 200
root_b_id_pool_size = 200
b_id_pool_size = 400

bookfile_dir = './app/static/book_file/'
hot_book_key = 'hot_books'

user_lib_text = 'user_lib:'


def add_user_id_pool(n, sql, is_lock=False):
    ids = []
    for a in range(n):
        ids.append(useridpool(is_lock=is_lock))
    print("user " + ("locked " if is_lock else "") + "id 生成完毕 开始添加到数据库")
    sql.session.add_all(ids)


def collect_user_id(user_id, sql):
    sql.session.add(useridpool(user_id=user_id))


def del_a_user_id_from_pool(sql):
    res = sql.session.query(useridpool.user_id).count()
    if res < user_id_pool_lock_size:
        add_user_id_pool(user_id_pool_lock_size - res, sql, True)
    if res < user_id_pool_size:
        add_user_id_pool(user_id_pool_size - res, sql)
    ret = sql.session.query(useridpool.user_id).filter(useridpool.is_lock == False).first()[0]
    sql.session.query(useridpool).filter(useridpool.user_id == ret).delete()
    return ret


def add_author_id_pool(n, sql, is_lock=False):
    ids = []
    for a in range(n):
        ids.append(authoridpool(is_lock=is_lock))
    print("author " + ("locked " if is_lock else "") + "id 生成完毕 开始添加到数据库")
    sql.session.add_all(ids)


def collect_author_id(author_id, sql):
    sql.session.add(authoridpool(author_id=author_id))


def del_a_author_id_from_pool(sql):
    res = sql.session.query(authoridpool.author_id).count()
    if res < author_id_pool_lock_size:
        add_author_id_pool(author_id_pool_lock_size - res, sql, True)
    if res < author_id_pool_size:
        add_author_id_pool(author_id_pool_size - res, sql)
    ret = sql.session.query(authoridpool.author_id).filter(authoridpool.is_lock == False).first()[0]
    sql.session.query(authoridpool).filter(authoridpool.author_id == ret).delete()
    return ret


def add_root_b_id_pool(n, sql):
    ids = []
    for a in range(n):
        ids.append(rootbookidpool())
    print("root book id 生成完毕 开始添加到数据库")
    sql.session.add_all(ids)


def collect_root_b_id(b_id, sql):
    sql.session.add(rootbookidpool(b_id=b_id))


def del_a_root_b_id_from_pool(sql):
    res = sql.session.query(rootbookidpool.b_id).count()
    if res < root_b_id_pool_size:
        add_root_b_id_pool(root_b_id_pool_size - res, sql)
    ret = sql.session.query(rootbookidpool.b_id).first()[0]
    sql.session.query(rootbookidpool).filter(rootbookidpool.b_id == ret).delete()
    return ret


def add_b_id_pool(n, sql):
    ids = []
    for a in range(n):
        ids.append(bookidpool())
    print("book id 生成完毕 开始添加到数据库")
    sql.session.add_all(ids)


def collect_b_id(b_id, sql):
    sql.session.add(bookidpool(b_id=b_id))


def del_a_b_id_from_pool(sql):
    res = sql.session.query(bookidpool.b_id).count()
    if res < b_id_pool_size:
        add_b_id_pool(b_id_pool_size - res, sql)
    ret = sql.session.query(bookidpool.b_id).first()[0]
    sql.session.query(bookidpool).filter(bookidpool.b_id == ret).delete()
    return ret


def add_user(user):
    with UsingAlchemy(log_label='添加用户') as sql:
        user_id = del_a_user_id_from_pool(sql)
        user.user_id = user_id
        user.activate_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(
            pytz.timezone("Asia/Shanghai"))
        sql.session.add(user)
    return user_id


def del_user(user_id):
    with UsingAlchemy(log_label='删除用户') as sql:
        try:
            sql.session.query(users).filter(users.user_id == user_id).delete()
            collect_user_id(user_id, sql)
        except TypeError:
            print("this user:", user_id, "not exist")
            return -1
    return 1


def select_user(user_id):
    with UsingAlchemy(log_label='获取用户信息') as sql:
        ret = sql.session.query(users).filter(users.user_id == user_id).first()
        sql.session.query(users).filter(users.user_id == user_id).update({
            "activate_time": datetime.datetime.utcnow().replace(
                tzinfo=pytz.utc).astimezone(
                pytz.timezone("Asia/Shanghai"))})
    try:
        return {'user_id': ret.user_id, 'user_name': ret.user_name, 'age': ret.age,
                "picture": ret.picture, "gender": ret.gender, "phone_number": ret.phone_number,
                "email": ret.email, "birthday": ret.birthday, "area": ret.area, 'user_describe': ret.user_describe,
                "activate_time": ret.activate_time, 'following_count': ret.following_count
                }
    except AttributeError:
        print("user not exist")
        return -1


def login_user(user_id, passwd):
    with UsingAlchemy(log_label='用户登录') as sql:
        ret = sql.session.query(users).filter(users.user_id == user_id).first()
        sql.session.query(users).filter(users.user_id == user_id).update({
            "activate_time": datetime.datetime.utcnow().replace(
                tzinfo=pytz.utc).astimezone(
                pytz.timezone("Asia/Shanghai"))})
    try:
        return passwd == ret.password
    except AttributeError:
        print("user not exist")
        return -1


def modify_update_info(update_dict):
    info = {}
    for key in update_dict.keys():
        if update_dict[key] != None:
            info[key] = update_dict[key]
    if info == {}:
        return False
    return info


def update_user(user_id, update_dict):
    update_dict = modify_update_info(update_dict)
    if update_dict != False:
        with UsingAlchemy(log_label='更新用户信息') as sql:
            ret = sql.session.query(users).filter(users.user_id == user_id).update(update_dict)
    else:
        print('update_dict is empty')


def add_author(author):
    with UsingAlchemy(log_label='添加作者') as sql:
        author_id = del_a_author_id_from_pool(sql)
        author.author_id = author_id
        sql.session.add(author)
    return author_id


def select_author(author_id):
    with UsingAlchemy(log_label='通过作者id获取作者信息') as sql:
        ret = sql.session.query(authores).filter(authores.author_id == author_id).first()
    try:
        return {'author_id': ret.author_id, 'author_name': ret.author_name, 'age': ret.age,
                "picture": ret.picture, "gender": ret.gender, "phone_number": ret.phone_number,
                "email": ret.email, "birthday": ret.birthday, "area": ret.area,
                'author_describe': ret.author_describe, 'follower_count': ret.follower_count,
                'works_count': ret.works_count}
    except AttributeError:
        print("not exist")
        return -1


def del_author(author_id):
    with UsingAlchemy(log_label='删除作者') as sql:
        try:
            ret = sql.session.query(booklib.b_id).filter(booklib.author_id == author_id).count()
            if ret != 0:
                print("此作者在数据库中拥有书籍，不能删除")
                return 0
            sql.session.query(authores).filter(authores.author_id == author_id).delete()
            collect_author_id(author_id, sql)
        except TypeError:
            print("not exist")
            return -1
    return 1


def login_author(au_id, passwd):
    with UsingAlchemy(log_label='作者登录') as sql:
        ret = sql.session.query(authores).filter(authores.author_id == au_id).first()
    try:
        return passwd == ret.password
    except AttributeError:
        print("author not exist")
        return -1


def update_author(author_id, update_dict):
    update_dict = modify_update_info(update_dict)
    if update_dict != False:
        with UsingAlchemy(log_label='更新作者信息') as sql:
            ret = sql.session.query(authores).filter(authores.author_id == author_id).update(update_dict)
    else:
        print('update_dict is empty')


def add_book_class(book_class):
    with UsingAlchemy(log_label='添加书籍种类编号') as sql:
        sql.session.add(book_class)


def add_language(language):
    with UsingAlchemy(log_label='添加支持语言') as sql:
        sql.session.add(language)


def add_book(book):
    with UsingAlchemy(log_label='在书籍库添加书籍') as sql:
        if book.b_id == None:
            b_id = del_a_b_id_from_pool(sql)
            book.b_id = b_id
        root_book_id = del_a_root_b_id_from_pool(sql)
        book.rootbookid = root_book_id
        book.is_original = "原作"
        rootbook = rootbooklib(root_b_id=root_book_id, orgin_b_id=b_id, info=list())
        rootbook.add2redis()
        sql.session.add(book)
        author = sql.session.query(authores).filter(authores.author_id == book.author_id).first()
        author.works_count += 1
        if not os.path.exists(bookfile_dir + str(b_id)):
            os.mkdir(bookfile_dir + str(b_id))
            with open(bookfile_dir + str(b_id) + '/.gitkeep', 'w') as fp:
                pass
    return b_id


def add_book_edition(root_b_id, book):
    with UsingAlchemy(log_label='在书籍库添加书籍') as sql:
        if book.b_id == None:
            b_id = del_a_b_id_from_pool(sql)
            book.b_id = b_id
        book.rootbookid = root_b_id
        book.is_original = "译作"
        keyname = book_lib_text + str(root_b_id)
        listindex = 0
        info = r0.lindex(keyname, listindex)
        info = json.loads(info)
        info.append(b_id)
        r0.lset(keyname, listindex, json.dumps(info))
        sql.session.add(book)
        author = sql.session.query(authores).filter(authores.author_id == book.author_id).first()
        author.works_count += 1
        sql.session.commit()
        if not os.path.exists(bookfile_dir + str(b_id)):
            os.mkdir(bookfile_dir + str(b_id))
            with open(bookfile_dir + str(b_id) + '/.gitkeep', 'w') as fp:
                pass
    return b_id


def update_book(b_id, update_dict):
    update_dict = modify_update_info(update_dict)
    if update_dict != False:
        with UsingAlchemy(log_label='在书籍库更新书籍信息') as sql:
            ret = sql.session.query(booklib).filter(
                and_(booklib.b_id == b_id)).update(
                update_dict)
    else:
        print('update_dict is empty')


def set_book_cover(b_id):
    path = bookfile_dir + str(b_id)
    if not os.path.exists(path):
        os.makdiers(path)
    return path + '/cover.'


def select_book(b_id):
    with UsingAlchemy(log_label='在书籍库获取书籍信息') as sql:
        ret = sql.session.query(booklib).filter(
            and_(booklib.b_id == b_id)).first()
    try:
        return {'b_id': ret.b_id, 'author_id': ret.author_id, 'lang_id': ret.lang_id,
                'bc_id': ret.bc_id, 'rootbookid': ret.rootbookid, 'name': ret.name,
                'desc': ret.desc, 'cover_path': ret.cover_path, 'create_time': ret.create_time}
    except AttributeError:
        print("not exist")
        return -1


def del_book(b_id):
    with UsingAlchemy(log_label='在书籍库删除书籍') as sql:
        res = select_book(b_id)
        if res == -1:
            print(b_id, '没有这本书')
            return -1
        rootbookid = res['rootbookid']
        print(rootbookid)
        sql.session.query(booklib).filter(booklib.b_id == b_id).delete()
        collect_b_id(b_id, sql)
        r0.delete(book_lib_content_text + str(b_id))
        keyname = book_lib_text + str(rootbookid)
        listindex = 0
        listindex1 = 1
        orginbookid = int(r0.lindex(keyname, listindex1))
        info = r0.lindex(keyname, listindex)
        info = json.loads(info)
        if orginbookid == b_id:
            if info == []:
                r0.delete(keyname)
                collect_root_b_id(rootbookid)
                return True
            b_id = orginbookid = info[0]
            r0.lset(keyname, listindex1, orginbookid)
        info.remove(b_id)
        r0.lset(keyname, listindex, json.dumps(info))
    return True


def select_orgin_book_by_b_id(b_id):
    with UsingAlchemy(log_label='在书籍库获取书籍信息') as sql:
        ret = sql.session.query(booklib).filter(
            and_(booklib.b_id == b_id)).first()
    try:
        orgin_id = r0.lindex(book_lib_text + str(ret.rootbookid), 1)
        return select_book(orgin_id)
    except AttributeError:
        print("not exist")
        return -1


def select_orgin_book_by_root_id(root_id):
    try:
        orgin_id = r0.lindex(book_lib_text + str(root_id), 1)
        return select_book(orgin_id)
    except AttributeError:
        print("not exist")
        return -1


def select_all_edition_b_id_by_b_id(b_id):
    with UsingAlchemy(log_label='在书籍库获取书籍信息') as sql:
        ret = sql.session.query(booklib).filter(
            and_(booklib.b_id == b_id)).first()
    try:
        info = r0.lindex(book_lib_text + str(ret.rootbookid), 0)
        info = json.loads(info)
        return info
    except AttributeError:
        print("not exist")
        return -1


def select_all_edition_b_id_by_root_id(root_id):
    try:
        info = r0.lindex(book_lib_text + str(root_id), 0)
        info = json.loads(info)
        return info
    except AttributeError:
        print("not exist")
        return -1


def mkdir_write(filepath, filename, content):
    pt = bookfile_dir + filepath + "/" + filename
    if not os.path.exists(bookfile_dir + filepath):
        os.makedirs(bookfile_dir + filepath)
    # with open(pt, 'rb') as f:
    #     result = chardet.detect(f.read())
    #     encoding = result['encoding']
    with open(pt, 'w', encoding='utf-8') as file:
        file.write(content)


def add_content(b_id, c_no, title, content):
    print('在书籍目录库添加信息')
    if c_no <= 0:
        print('章节数不能小于等于0')
        return 0
    ret = select_book(b_id)
    if ret == -1:
        return -1
    mkdir_write(str(ret['b_id']), str(c_no) + '.txt', content)
    llen = r0.llen(book_lib_content_text + str(b_id)) - 1
    while llen < c_no:
        r0.rpush(book_lib_content_text + str(b_id), '')
        llen += 1
    r0.lset(book_lib_content_text + str(b_id), c_no, title)
    return 1


def update_content(b_id, c_no, title, content):
    print('在书籍目录库更新信息')
    if c_no <= 0:
        print('章节数不能小于等于0')
        return 0
    ret = select_book(b_id)
    if ret == -1:
        return -1
    content_path = str(ret['b_id']) + '/' + str(c_no) + '.txt'
    r0.lset(book_lib_content_text + str(b_id), c_no, title)
    with open(bookfile_dir + '/' + content_path, 'w') as file:
        content = file.write(content)
    return 1


def select_bookcontent(b_id, c_no):
    print('在书籍目录库获取信息')
    if c_no <= 0:
        print('章节数不能小于等于0')
        return 0
    ret = select_book(b_id)
    if ret == -1:
        return -1
    content_path = str(ret['b_id']) + '/' + str(c_no) + '.txt'
    try:
        with open(bookfile_dir + '/' + content_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return -2
    try:
        ret = r0.lindex(book_lib_content_text + str(b_id), c_no)
        if ret == None:
            return -1
        return [ret, content]
    except Exception:
        return -3


def select_all_lang_id():
    with UsingAlchemy(log_label='获取所有语言编号') as sql:
        ret = sql.session.query(languages).all()
        res = list()
        for id in ret:
            res.append(id.lang_id)
    return res


def select_this_author_s_all_book(author_id):
    with UsingAlchemy(log_label='获取这位作者的所有书籍') as sql:
        ret = sql.session.query(booklib).filter(booklib.author_id == author_id).all()
        res = list()
        for book in ret:
            res.append({'b_id': book.b_id, 'author_id': book.author_id, 'lang_id': book.lang_id,
                        'bc_id': book.bc_id, 'rootbookid': book.rootbookid, 'name': book.name,
                        'desc': book.desc, 'cover_path': book.cover_path, 'create_time': book.create_time,
                        'is_original': book.is_original})
    return res


def search_book(book_name):
    with UsingAlchemy(log_label='在书籍库模糊查询') as sql:
        book_name = "%" + book_name + "%"
        ret = sql.session.query(booklib).filter(booklib.name.like(book_name)).all()
        res = list()
        for book in ret:
            res.append({'b_id': book.b_id, 'author_id': book.author_id, 'lang_id': book.lang_id,
                        'bc_id': book.bc_id, 'rootbookid': book.rootbookid, 'name': book.name,
                        'desc': book.desc, 'cover_path': book.cover_path, 'create_time': book.create_time})
    return res


def select_contents_by_a_book(b_id):
    print('在书籍目录库获取目录信息')
    ret = select_book(b_id)
    if ret == -1:
        return -1
    ret = r0.lrange(book_lib_content_text + str(b_id), 1, -1)
    if ret == None:
        return -1
    return list(ret)


def set_hot_book(hot_book_list):
    print('设置热门图书')
    r0.set(hot_book_key, json.dumps(hot_book_list))


def select_hot_book():
    print('获取热门图书')
    ret = r0.get(hot_book_key)
    if ret == None:
        return -1
    return json.loads(ret)


def add_user_read_history(user_id, b_id, c_no, t):
    print('添加用户' + str(user_id) + '阅读书籍' + str(b_id) + '记录')
    now = str(str(datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))))
    record = [b_id, c_no, t]
    r0.rpush(user_lib_text + str(user_id) + ':history', json.dumps(record))


def get_user_read_history(user_id):
    print('获取用户' + str(user_id) + '阅读记录')
    histories = list(r0.lrange(user_lib_text + str(user_id) + ':history', 0, -1))
    res = []
    for record in histories:
        res.append(json.loads(record))
    return res


def user_create_a_collection_lib(user_id, libname):
    print('用户' + str(user_id) + '创建收藏夹' + libname)
    r0.set(user_lib_text + str(user_id) + ':collction_lib:' + libname, json.dumps([]))


def get_name_from_key(key: str):
    l = key.split(':')
    return l[-1]


def user_get_all_collection_lib(user_id):
    print('用户' + str(user_id) + '获取所有收藏夹')
    lib = r0.keys(user_lib_text + str(user_id) + ':collction_lib:*')
    res = []
    for key in lib:
        res.append(get_name_from_key(key))
    return res


def user_delate_a_collection_lib(user_id, libname):
    print('用户' + str(user_id) + '删除收藏夹' + libname)
    r0.delete(user_lib_text + str(user_id) + ':collction_lib:' + libname)


def user_collect_a_book(user_id, libname, b_id):
    print('用户' + str(user_id) + '在收藏夹' + str(libname) + '收藏书籍' + str(b_id))
    try:
        list = json.loads(r0.get(user_lib_text + str(user_id) + ':collction_lib:' + libname))
    except TypeError:
        user_create_a_collection_lib(user_id, libname)
        list = []
    if b_id in list:
        print(b_id, '已存在于收藏夹')
        return False
    list.append(b_id)
    r0.set(user_lib_text + str(user_id) + ':collction_lib:' + libname, json.dumps(list))
    return True


def user_delate_a_collected(user_id, libname, b_id):
    print('用户' + str(user_id) + '在收藏夹' + str(libname) + '删除收藏书籍' + str(b_id))
    list = []
    list = json.loads(r0.get(user_lib_text + str(user_id) + ':collction_lib:' + libname))
    if b_id not in list:
        print(b_id, '已不存在于收藏夹')
        return False
    list.remove(b_id)
    r0.set(user_lib_text + str(user_id) + ':collction_lib:' + libname, json.dumps(list))
    return True


def get_user_collection(user_id, libname):
    print('获取用户' + str(user_id) + '的收藏夹' + str(libname) + '的内容')
    list = json.loads(r0.get(user_lib_text + str(user_id) + ':collction_lib:' + libname))
    return list


def get_info_class(id):
    with UsingAlchemy(log_label='info_class') as sql:
        ret = sql.session.query(bookclass).filter(
            and_(bookclass.bookclass_id == id)).first()
    return ret.class_name


def get_info_lang(id):
    with UsingAlchemy(log_label='info_lang') as sql:
        ret = sql.session.query(languages).filter(
            and_(languages.lang_id == id)).first()
    return ret.lang_name


def add_barrages(user_barrage):
    with UsingAlchemy(log_label='添加用户弹幕') as sql:
        now = str(str(datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))))
        user_barrage.create_time = now
        sql.session.add(user_barrage)


def select_barrages():
    with UsingAlchemy(log_label='获取主页弹幕信息') as sql:
        ret = sql.session.query(user_barrage).order_by(user_barrage.create_time.desc()).all()
        res = list()
        for i in ret[:10]:
            user_name = select_user(i.user_id).get('user_name')
            res.append({'user_id': i.user_id, 'user_name': user_name, 'barrage': i.barrage, 'time': i.create_time})
    return res


def add_user_book_barrage(user_book_barrage):
    with UsingAlchemy(log_label='添加用户弹幕') as sql:
        now = str(datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai")))
        user_book_barrage.create_time = now
        sql.session.add(user_book_barrage)


def select_barrage_by_b_id(book_id):
    with UsingAlchemy(log_label='获取该书籍评论') as sql:
        ret = sql.session.query(user_books_barrage).filter(user_books_barrage.book_id == book_id).all()
        res = list()
        for i in ret:
            user_name = select_user(i.user_id).get('user_name')
            res.append({'user_id': i.user_id, 'user_name': user_name, 'barrage': i.barrage, 'time': i.create_time})
    return res


def add_user_follow_author(fan):
    with UsingAlchemy(log_label='添加用户关注作者') as sql:
        user = sql.session.query(users).filter(users.user_id == fan.user_id).first()
        author = sql.session.query(authores).filter(authores.author_id == fan.author_id).first()
        if user and author:
            sql.session.add(fan)
            user.following_count += 1
            author.follower_count += 1
            sql.session.commit()


def remove_user_unfollow_author(user_id, author_id):
    with UsingAlchemy(log_label='用户取消关注作者') as sql:
        user = sql.session.query(users).filter(users.user_id == user_id).first()
        author = sql.session.query(authores).filter(authores.author_id == author_id).first()
        if user and author:
            f = sql.session.query(fan).filter(
                fan.user_id == user.user_id, fan.author_id == author.author_id
            ).first()
            if f:
                sql.session.delete(f)
                user.following_count -= 1
                author.follower_count -= 1
                sql.session.commit()


def get_user_followed_authors(user_id):
    with UsingAlchemy(log_label='用户获取所有关注作者') as sql:
        user = sql.session.query(users).filter(users.user_id == user_id).first()
        if user:
            followed_authors = sql.session.query(authores).join(fan).filter(fan.user_id == user.user_id).all()
            res = list()
            for author in followed_authors:
                res.append({'author_id': author.author_id, 'author_name': author.author_name,
                            'age': author.age, 'gender': author.gender, 'follower_count': author.follower_count,
                            'works_count': author.works_count, 'area': author.area})
            return res


__all__ = ['users', 'authores', 'booklib',
           'user_id_pool_size', 'user_id_pool_lock_size', 'author_id_pool_size',
           'author_id_pool_lock_size', 'root_b_id_pool_size', 'b_id_pool_size',
           'add_user', 'del_user', 'select_user', 'login_user', 'update_user',
           'add_author', 'select_author', 'del_author', 'login_author',
           'update_author', 'add_book', 'add_book_edition', 'update_book',
           'set_book_cover', 'select_book', 'add_content', 'update_content',
           'select_bookcontent', 'select_all_lang_id', 'select_this_author_s_all_book',
           'search_book', 'del_book', 'select_orgin_book_by_b_id', 'select_orgin_book_by_root_id',
           'select_all_edition_b_id_by_b_id', 'select_all_edition_b_id_by_root_id',
           'set_hot_book', 'select_hot_book', 'select_contents_by_a_book',
           'add_user_read_history', 'get_user_read_history',
           'user_collect_a_book', 'user_delate_a_collected',
           'user_create_a_collection_lib', 'user_delate_a_collection_lib',
           'get_user_collection', 'user_get_all_collection_lib',
           'get_info_class', 'get_info_lang', 'add_barrages', 'select_barrages', 'add_user_book_barrage',
           'select_barrage_by_b_id', 'add_book_class', 'add_language', 'add_user_follow_author',
           'remove_user_unfollow_author', 'get_user_followed_authors']
