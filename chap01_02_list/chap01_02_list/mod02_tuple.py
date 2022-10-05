
## 튜플(tuole)
# 값을 소괄호로 생성한다.
# 리스트처럼 인덱스가 있다.
# 리스트와 달리 값을 수정할 수 없다.

if __name__ == '__main__':
    tur = ()
    tur = (10, 11, 12, 13, 14)

    print(tur[0:5])
    print(tur[0:len(tur)])
    print()

    # tur.append(6) #값을 추가할 수 없음(오류)

    # 값 사용, for문으로 값을 하나씩 꺼내서 출력[리스트와 동일]
    for t in tur:
        print(t, end=' ')
    print()

    # 튜플에서 인덱스로 접근하여 추출
    for i in range(0, len(tur)):
        print(tur[i], end=' ')
    print()

    # 2차원 튜플 출력하기
    dim2 = ((1,2,3),
            (11,12,13),
            (12,22,23))

    for i in range(0,3):
        for j in range(0,3):
            print(dim2[i][j], end=' ')
    print()

