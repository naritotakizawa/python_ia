def is_prime(number):
    # 引数のnumberが素数ならTrueを返す
    for j in range(2, number):
        # print(f'  j={j}')
        if i % j == 0:
            return False

    # 割り切れなかったら（素数じゃなかったら）ここに到達する
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i)

