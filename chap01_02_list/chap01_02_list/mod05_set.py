
## 세트 Set
# 딕셔너리에서 키만 모아놓은 특수한 형태
# 중복되지 않으며 자료 생성시 중괄호 {}를 사용하지만 : 는 없다. 즉 키만 존재 {key1, key2, ...}

# 랜덤은 별도의 라이브러리가 필요함
import random

numSet = set()

# set() 자료구조를 이용하여 중복 없이 난수 7개를 생성하는 함수
def get_number():
    while len(numSet) <= 6:
        #numSet.add(random.randrange(0, 46)) # 0부터 46미만의(미포함) 숫자 중에서 랜덤 생성
        numSet.add(random.randint(1, 45)) # 1부터 45까지의(포함) 정수 중에서 랜덤 생성

if __name__ == '__main__':
    mySet = {1,2,3,4,3,5,2}
    print(type(mySet)) #<class 'set'>
    print(mySet) # 중복이 제거됨

    salesItems = {'삼각김밥', '바나나', '도시락', '삼각김밥', '도시락', '컵라면', '생수'}
    print(salesItems)

    # set() 함수
    # - 리스트, 튜플, 딕셔너리 등을 세트로 변환 시켜줌
    # 세트의 특성은 인덱스가 없다는 것이다.
    # 다음은 학생들의 형액형에 대한 데이터이다.
    # for문을 이용하여 각 형액형 별 학생수와 전체 학생수를 구하시오.
    list = ['A', 'B', 'A', 'O', 'A', 'AB', 'O', 'A', 'A', 'O', 'B', 'AB']
    mySet = set(list)
    print(type(mySet), mySet)

    count = 0
    tot = 0
    countList = []
    dic = {}            # 딕셔너리 선언

    for b in set(list): # 중복이 제거된 혈액형
        for l in list:  # 전체 학생의 햘액형
            if b == l:
                count += 1
                tot += 1
        dic[b] = count # 딕셔너리에 추가
        count = 0

    for (key, value) in dic.items():
        print('{0}형 : {1}명'.format(key, value))
    print('전체 인원수 : {0}'.format(tot))
    print()

    dic = {1:'홍길동', 2:'임꺾정', 3:'김두한', 4:'최덕팔'}
    mySet = set(dic)
    print(mySet)
    for key in mySet:
        print(dic[key])
    print()

    # 교집합/합집합
    mySet2 = {1,2,3,4,5}
    mySet3 = {4,5,7,7,8}
    mySet4 = mySet2 & mySet3
    mySet5 = mySet2 | mySet3

    print('교집합 : ', mySet4)
    print('합집합 : ', mySet5)

    # in, not in
    print(6 in mySet2)
    print(6 not in mySet2)

    # 값 추기 add()함수
    mySet2.add(6)
    print(mySet2)

    # 값 제거 remove() 함수
    mySet2.remove(6)
    print(mySet2)

    # 값 제거 discard() 함수, 제거할 값이 없어도 오류 안남.
    #mySet2.remove(99) # 요소가 존재하지 않아 오류
    mySet2.discard(99) # 요소가 존재라지 않아도 오류가 나지 않음.

    # set() 함수를 활용한 난수 생성
    get_number()
    print(f'중복 없이 생성된 난수 : {numSet}')