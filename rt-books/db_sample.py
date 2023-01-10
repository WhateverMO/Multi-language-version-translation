from Database import *

hot_book_list = []

u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
uu_id = u_id
update_user(u_id, {'user_name': "李四"})
if login_user(u_id, "123456"):
    print("right password!")
if login_user(u_id, "123456#") == False:
    print("wrong password!")
if login_user(u_id + user_id_pool_size * 10, "123456") == -1:
    print("not exist!")
ret = select_user(u_id)
print(ret)
ret = select_user(u_id + user_id_pool_size * 10)
print(ret)
u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
print(del_user(u_id))
print(del_user(u_id - user_id_pool_size))
u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
au_id = add_author(authores(author_name="作者张三", author_describe="我成作者啦", password="123456"))
print(del_user(u_id))
print(login_author(au_id, '123456'))
print(login_author(au_id-author_id_pool_size*10, '123456'))
print(login_author(au_id, '12345'))
u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
au_id = add_author(authores(author_name="作者张三", author_describe="我成作者啦", password="123456"))
print(select_author(au_id))
print(select_author(au_id - author_id_pool_size))
au_id = add_author(authores(author_name="作者张三", author_describe="我成作者啦", password="123456"))
u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
temp_gai_author = dict()
temp_gai_author['author_describe'] = "我改了签名"
update_author(au_id, temp_gai_author)
print(del_author(au_id))
print(del_author(au_id - author_id_pool_size))



u_id = add_user(users( user_name="张三", user_describe="我是张三haha", password="123456"))
au_id = add_author(authores(author_name="作者张三", author_describe="我成作者啦", password="123456"))
b_id = add_book(booklib(author_id=au_id, name="第一本书", lang_id=1, bc_id=1))
add_user_read_history(uu_id,b_id)
hot_book_list.append(b_id)
b_id = add_book(booklib(author_id=au_id, name="第二本书", lang_id=1, bc_id=1))
add_user_read_history(uu_id,b_id)
hot_book_list.append(b_id)
b_id = add_book_edition(select_book(b_id)['rootbookid'], booklib(author_id=au_id, name="第二本书##", lang_id=1, bc_id=1))
add_user_read_history(uu_id,b_id)
hot_book_list.append(b_id)
print('#')
print(select_orgin_book_by_b_id(b_id))
print(select_orgin_book_by_root_id(select_book(b_id)['rootbookid']))
print(select_all_edition_b_id_by_b_id(b_id))
print(select_all_edition_b_id_by_root_id(select_book(b_id)['rootbookid']))

print(del_author(au_id))
print(select_book(b_id - b_id_pool_size * 10))
info = select_book(b_id)
update_book(info['b_id'], {'lang_id': 2})
print(set_book_cover(b_id))
print(add_content(b_id - b_id_pool_size * 10, 1,'第一章', '文本'))
print(add_content(b_id, 1,'第一章', '文本'))
print(add_content(b_id, 2,'第2章', '文本'))
print(add_content(b_id, 3,'第3章', '文本'))
print(update_content(b_id - b_id_pool_size * 10, 1,'第一章！', '1234'))
print(update_content(b_id, 1,'第一章！', '1234'))
print(select_bookcontent(b_id, 1))
print(select_bookcontent(b_id, -1))

print('####')
print(select_contents_by_a_book(b_id))

print(select_all_lang_id())
print(select_this_author_s_all_book(au_id))
print(search_book('一'))

set_hot_book(hot_book_list)
print(select_hot_book())
hot_book_list = [12,13,15]
set_hot_book(hot_book_list)
print(select_hot_book())

print(get_user_read_history(uu_id))

user_create_a_collection_lib(u_id,'my like list')
user_create_a_collection_lib(u_id,'my like list!')
user_create_a_collection_lib(u_id,'my like list!!')
user_delate_a_collection_lib(u_id,'my like list!')

print(user_collect_a_book(u_id, 'my like list', b_id))
print(user_collect_a_book(u_id, 'my like list', b_id))
print(user_collect_a_book(u_id, 'my like list', b_id+1))
print(user_delate_a_collected(u_id, 'my like list', b_id))
print(user_collect_a_book(u_id, 'my like list', b_id))
print(user_delate_a_collected(u_id, 'my like list', b_id-b_id_pool_size*10))
print(get_user_collection(u_id, 'my like list'))