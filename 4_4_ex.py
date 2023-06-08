# 文字列の2023 といった内容が入る
user_input_year = input()

# 数値の2023になる
year = int(user_input_year)

# 数値の2024になる (数値同士の足し算なので、エラーにならない)
next_year = year + 1


# 愚直に書く例
# print('今は' + str(year) + '年です。来年は' + str(next_year) + '年です')

string_year = str(year)
string_next_year = str(next_year)

print(f'今は{string_year}年です。来年は{string_next_year}年です')

# これでもかけちゃう
# print(f'今は{year}年です。来年は{next_year}年です')