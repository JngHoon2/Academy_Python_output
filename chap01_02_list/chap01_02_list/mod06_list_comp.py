
## 리스트 컴프리핸션(comprehension) 축약, 압축

if __name__ == '__main__':
    # 리스트를 사용한 저장/출력
    data =[]
    for i in range(1, 11):
        data.append(i)
    print(data)

    # 리스트 컴프리핸션
    # 첫 번쨰 k는  data에 저장되는 k
    # 뒤의 k는 range함수에서 하나씩 꺼내온 값으로 두 값의 이름은 같아야 함.
    data = [k for k in range(1, 11)]
    print('data type : ', type(data))
    print('1. ', data)

    # 1부터 10까지 숫자 중 2의 배수만을 컴프리핸션으로 생성
    data = [k for k in range(1, 11) if k % 2 == 0]
    print('2. ',data)

    # 1부터 100까지의 숫자 중 20 < x <= 50 사이에 있는 짝수만 선별[컴프리핸션]
    data = [k for k in range(1, 101) if k > 20 and k <= 50 and k % 2 == 0]
    print('3. ', data)

    # 리스트를 활용한 컴프리핸션
    originalList = [1,2,3,4,5,6,7,8,9,10]
    doubleList = [2 * x for x in originalList]
    print('4. ', doubleList)

    # 이중 for문을 활용한 컴프리핸션
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    flat = [x for row in matrix for x in row] # 왼쪽에서 오른쪽 순으로 실행
    print('5. ', flat)