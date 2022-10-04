
#### 연산자[operator]

if __name__ == '__main__':
    print(1 + 1)
    print(2 * 3)
    print(6 / 2)
    print(9 / 4)
    print(9 // 4)
    print(2 ** 3)
    print(5 % 3)

    # 파이썬은 증감연산자가 없음.
    num = 70
    num += 1

    print(num)
    # print(num += 1)

    # 관계 연산자
    print(2 > 3)
    print(5 <= 5)
    print(2 != 3)
    print(not 2 == 3)
    print(not 2 != 3)

    print((2 > 3) and (4 < 5))
    print((2 < 3) & (4 < 5))
    print((2 == 3) or (4 < 5))
    print((2 == 3) | (4 < 5))

