#### pandas(Python Data Analysys Library) Dataframe ####
# 1. R의 dataframe 데이터 타입을 참고하여 만든 것이 바로 pandas dataframe
# 2. pandas Dataframe은 테이블 형식의 (행, 열)데이터(그리드)를 다룰 때 사용한다.
# 3. dataframe의 3요소는 컴럼, 데이터(로우), 인덱스가 있다.
# 4. dataframe은 다음과 같은 다양한 데이터 타입으로부터 만들 수 있다.
# - ndarray, dictionary, dataframe, series, list
# 5. DataFrame 객체를 각 컬럼에 대한 데이터를 저정한 후 딕셔너리를 Dataframe 클래스의
# 생성자 인자로 넘겨주면 Dataframe 객체가 생성된다.
# 6. Dataframe은 시리즈(1차원 배열)로 구성되어 있다.

# [1] 판다스 라이브러리 불러오기
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# [2] Dataframe 만들기
# 1. DataFrame에 대한 입력으로 2차원 리스트를 만든다.
list = [[1,2,3,4,],
        [10, 20, 30, 40],
        [100,200,300,400],
        [1000,2000,3000,4000],
        [10000,20000,30000,40000]]

# 2차원 리스트로 판다스 dataframe 만들기
# 행 index : 행을 결정짓는 유일한 이름
df1 = pd.DataFrame(list, index=['일단위','십단위','백단위','천단위','만단위'])
print("1. 판다스 전체 모습 : ")
print(df1)
print()

# 2. 행 인덱스(index)로 반복
print("2. iterrows() 반복 : ")
# iterrows() : DataFrame 행을 (인덱스, 시리즈) 쌍으로 반복
for (index, row) in df1.iterrows(): # 시리즈 쌍으로 반복
    # row[컬럼 인덱스 번호]
    print(index, row[0], row[1], row[2], row[3])
print()

# 3. 특정 행 조회, 행 범위 별로 조회(행 슬라이싱)
# [오류] df1['값']하면 컬럼명으로 조회하기 때문에 오류
print('3. df1[\'백단위\'] : ', df1[0])
print()

print('4. df1[\'백단위\':\'백단위\'] : ') # 한 행 조회
print(df1['백단위' : '백단위']) # 한 행 조회

# 행의 이름으로 슬라이싱(범위로 조회) 만단위 포함
print('5. df1[\'일단위\':\'만단위\'] : 일단위 ~ 만단위 까지')
print(df1['일단위' : '만단위'])

# 행의 범위 슬라이싱(만단위 빠짐 주의!, 미포함)
print('6. df1[0:4] : 0부터 4직전까지')
print(df1[0:4])
print()

print('7. len(df1)', len(df1), df1.shape) # dataframe 행수(len(df1))와 전체적인 모습
# 3. 열(컬럼)의 전체 값 조회
print()
print('8. df[0] #0번째 컬럼의 모든 값')
print(df1[0])
print()
print('9.df1[1] #1번째 컬럼의 모든 값')
print(df1[1])
print()

# 4. iteritems()을 통한 행 반복
print('10.1 df1.iteritems() : ', type(df1.iteritems())) #<class 'generator'>
print()

# print('11. df1.iteritems()')
for col_name, col in df1.iteritems(): #col_name : 컬럼 명, col : 컬럼값 전체 Series
    print(f"{col_name}번째 - 컬럼값 {col[0]} {col[1]} {col[2]} {col[3]}")
    # print(f"{col_name}번째 - 컬럼값 {col.values}.")
print()

print("12. 일자별 판매 데이터")

# 5. 일자별 온라인 + 오프라인 판매금액 관련 dataframe 예제
dates = ['10/01','10/02','10/03','10/04','10/05','10/06']
online_sales = [300, 280, 350, 650, 500, 450]
offline_sales = [150, 130, 210, 130, 100, 200]

df = pd.DataFrame({"date" : dates,
                   "on_sales" : online_sales,
                   "off_sales" : offline_sales})
print(df)
print()