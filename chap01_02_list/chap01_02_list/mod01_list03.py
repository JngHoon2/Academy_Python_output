
#[2차원 리스트]
if __name__ == '__main__':
    print('------------------------------ 3 * 4 형태의 2차원 리스트 ------------------------------')
    two_list = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]

    for i in range(0, 3):
        for j in range(0, 4):
            print(two_list[i][j], end=' ')
        print()
    print()

    for i, j in enumerate(two_list):
        print(i, j)
    print()


    list1 = []
    list2 = []
    value = 0

    for i in range(3):
        for j in range(4):
            value += 1
            list1.append(value)
        list_copy = list1.copy()
        list2.append(list_copy)
        list1.clear()

    for i, j in enumerate(list2):
        print(i, j)
    print()


    #[2] 다음 데이터를 참고라여 2차원 리스트를 만들고 출력하세요.
    name_list = [['김순택', 23], ['정연희', 30], ['최우철', 40]]

    for i, name in enumerate(name_list):
        print('{0} {1}'.format(name[0], name[1]))


    list_num = [1,2,3,4,5]
    print(list_num[1:4])