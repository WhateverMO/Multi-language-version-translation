from Database import *

hot_book_list = []

u_id = add_user(users(user_name="秋海棠", user_describe="我是秋海棠", password="716300",
                      picture='http://localhost:5000/static/avatar_file/b2.jpg'))

au_id1 = add_author(
    authores(author_name="刘慈欣", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id2 = add_author(
    authores(author_name="东野圭吾", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id3 = add_author(
    authores(author_name="余华", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id4 = add_author(
    authores(author_name="J.K.罗琳", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id5 = add_author(
    authores(author_name="曹雪芹", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id6 = add_author(
    authores(author_name="卡勒德·胡赛尼", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id7 = add_author(authores(author_name="加西亚·马尔克斯", password="123456",
                             picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id8 = add_author(
    authores(author_name="石悦", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))
au_id9 = add_author(
    authores(author_name="圣埃克苏佩里", password="123456", picture='http://localhost:5000/static/avatar_file/b2.jpg'))

b_id1 = add_book(booklib(author_id=au_id1, name="三体", lang_id=1, bc_id=4,
                         desc='这是一部描述地球人类文明和三体文明的恩怨纠葛的硬科幻小说',
                         cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id2 = add_book(
    booklib(author_id=au_id2, name="白夜行", lang_id=1, bc_id=6, desc='这是一部探讨人性、正义和罪恶的悬疑推理小说。',
            cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id3 = add_book(
    booklib(author_id=au_id3, name="活着", lang_id=1, bc_id=2, desc='这是一部反映中国农村社会变迁的现实主义小说',
            cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id4 = add_book(booklib(author_id=au_id4, name="哈利·波特与魔法石", lang_id=1, bc_id=5,
                         desc='这是一部讲述一个魔法世界的奇幻冒险小说',
                         cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id5 = add_book(
    booklib(author_id=au_id5, name="红楼梦", lang_id=1, bc_id=1, desc='这是一部描写清代贵族家庭衰落的古典小说文学名著',
            cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id6 = add_book(
    booklib(author_id=au_id6, name="追风筝的人", lang_id=1, bc_id=2, desc='这是一部展现阿富汗历史和文化的感人小说',
            cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id7 = add_book(
    booklib(author_id=au_id7, name="百年孤独", lang_id=1, bc_id=1, desc='这是一部运用魔幻现实主义手法的拉美文学代表作',
            cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id8 = add_book(booklib(author_id=au_id2, name="解忧杂货店", lang_id=1, bc_id=1,
                         desc='这是一部通过一个神秘的杂货店回答人们烦恼的温馨小说',
                         cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id9 = add_book(booklib(author_id=au_id8, name="明朝那些事儿", lang_id=1, bc_id=3,
                         desc='这是一部用幽默的语言讲述明朝历史的网络小说',
                         cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
b_id10 = add_book(booklib(author_id=au_id9, name="小王子", lang_id=1, bc_id=30, desc='这是一部寓言式的儿童文学经典',
                          cover_path='http://localhost:5000/static/cover_file/b2.jpg'))
hot_book_list.append([b_id1, b_id2, b_id3, b_id4])
set_hot_book(hot_book_list)
