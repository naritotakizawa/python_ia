dic = {
    '商品A': 3,
    '商品B': 10,
    '商品C': 7,
    '商品D': 5
}

print('商品一覧')
# 辞書のkeysメソッドは、for key in ['商品A', '商品B', '商品C', '商品D']
for key in dic.keys():
    print(key)

# キーの一覧を取り出すときは、わざわざkeysメソッド呼ばないほうが多い
# for 変すうめい in 辞書オブジェクト
for key in dic:
    print(key)


print('\n商品と在庫数の一覧')
for key, value in dic.items():  # このitemsを使ったを暗記したい
    print('商品名：' + key + '\t在庫数：' + str(value))


# dic.items()
# 次のようなリストを作る
# tuple_list = [
#     ('商品A', 3),
#     ('商品B', 10),
#     ('商品C', 7),
#     ('商品D', 5)
# ]
#
# for key, value in tuple_list:
#     print(key)
#     print(value)
#
#
# key, value = ['商品A', 3]
