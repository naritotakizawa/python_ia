# 変数の値は最後に代入された値に書き変わります
# '滝澤'についていたnameというラベルを、'成人'に張り替えた、そんなイメージです
name = '滝澤'
name = '成人'
print(name)



name = '滝澤'

# 必ず = の右側から実行されるので、 name + '成人' がまず作成される
# 変数は、足し算など自由にできる(型が同じならば！)
# name + '成人'　の結果に、=の左側のnameという名前をっつける
name = name + '成人'
print(name)  # →滝澤成人と表示される


# 変数同士を足し算した結果も、変数に代入できる
# わかりやすい変数名をつけると、読みやすくなります
first_name = 'narito'
last_name = 'takizawa'
full_name = first_name + last_name
print(full_name)
# → naritotakizawaと表示される


