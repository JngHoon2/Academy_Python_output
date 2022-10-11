import pandas as pd

### 판다스 : 데이터분석 라이브러리
# Serires : 판다스에서 기본으로 제공하는 자료구조
# 1차원의 집합 자료형 구조이다.
# 시리즈는 엑셀의 컬럼과 같으며 인덱스를 갖는다.
# 시리즈의 인덱스는 name 속성을 갖으며 숫자, 문자, 모두 가능하고 이름도 바꿀 수 있다.

# 시리즈 만들기
# [1] 리스트를 통해서 만들기, 인덱스도 설정
data = pd.Series(['김영수', '정대욱', '민형기'], index=['1', '2', '3'])

# 1. 인덱스로 조회 data['1'], 시리즈['인덱스']
print('1.1 data[\'1\'] : ', data['1'])
print('1.2 data[\'2\'] : ', data['2'])
print('1.3 data[\'3\'] : ', data['3'])
print()

# 2. 명시적으로 제공한 인덱스로 슬라이싱 조회 data['1':'3']
print('2. data[\'1\' : \'3\'] : ')
print(data['1':'3']) #1번째 ~ 3번째까지(3번째 포함)
print()

print('3. data[0:2] : ')
print(data[0:2]) #0번째 ~ 2번째 직전까지(2번째 미포함)
print()

print("4. 값 data.values : ", data.values)

print("5. 인덱스 data.index : ", data.index)
print()

print("6. 시리즈 반복 : ")
for i in data:
    print(type(i), i)
print()

print("7. 카카오 일별 종가 전체 : ")
kakao = pd.Series([92600, 92400, 92100, 94300, 92300], ['2016-02-19', '2016-02-18', '2016-02-17', '2016-02-16', '2016-02-15'])
print(kakao)
print()

print("8. 카카오 날짜 반복문 : ")
for i in kakao.index:
    print(i)
print()

print("9. 카카오 종가 반복문 : ")
for v in kakao.values:
    print(v)
print()

print("10. 카카오 일별 종가 반복문 : ")
sum = 0
avg = 0.0
for i, w in kakao.items():
    print(i, w)
    sum += w
avg = sum / kakao.size
print("합계 : {0}, 평균 : {1}".format(sum, avg))

#[2] 딕셔너리를 통한 시리즈 만들기
sd = pd.Series({'이정후' : 0.352, '피렐라' : 0.341, '박건우' : 0.337})
print(sd)
print()

print('21. 시리즈 반복 인덱스(키) ')
for i in sd.index:
    print(i)
print()

print('22. 시리즈 반복 값')
for i in sd.values:
    print(i)

print('23. 시리즈 전체 키(sd.keys()) : ', sd.keys())
print('24. 시리즈 전체 값(sd.values()) : ', sd.values)
print('25. 시리즈 인덱싱(key 접근) : ', sd['이정후'], sd['피렐라'], sd['박건우'])
print('26. 시리즈 인덱싱(기본 인덱스 접근) : ', sd[0], sd[1], sd[2])
print()

