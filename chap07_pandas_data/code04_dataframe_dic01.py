
import pandas as pd
import numpy as np

##[3] 딕셔너리 형태로 DataFrame 반환

# 1. 딕셔너리 형태의 데이터프레임 생성
raw_data = {'col0' : [1,2,3,4],
            'col1' : [10,20,30,40],
            'col2' : [100,200,300,400]
            }

data = pd.DataFrame(raw_data)
print('1. 딕셔너리 향태의 데이터프레임')
print(data)
print()

# iterrows() : Dataframe 행을 (인덱스, 시리즈) 쌍으로 반복
print("2. iterrows()를 통한 행 반복")
for (idx, col) in data.iterrows():
    print(idx, col[0], col[1], col[2])
print()

print("3. range() + loc[] 통한 행 반복")
for i in range(len(data)):
    print(data.loc[i, 'col0'], data.loc[i, 'col1'], data.loc[i, 'col2'])
print()

print("3.2 range(len(df)) 행 반복 - data.iloc[0,0]으로 접근")
for i in range(len(data)):
    print(i, data.iloc[i, 0], data.iloc[i, 1], data.iloc[i, 2])
print()

name_series = pd.Series(['김수안', '김수정', '박동윤', '강이안', '강지안'])
age_series = pd.Series([19, 23, 22, 19, 16])
sex_series = pd.Series(['여', '여', '남', '여', '남'])
grade_series = pd.Series([4.35, 4.23, 4.25, 4.37, 4.25])

df = pd.DataFrame({
    '이름' : name_series,
    '나이' : age_series,
    '성별' : sex_series,
    '평점' : grade_series
})

# .itertuples()
print('.itertuples()')
for row in df.itertuples():
    print(row[1], row[2], row[3], row[4])
print()

# .range(len(df)) + loc
print('.range(len(df)) + loc')
for i in range(len(df)):
    print(df.loc[i, '이름'], df.loc[i, '나이'], df.loc[i, '성별'], df.loc[i, '평점'])
print()

# range(len(df)) + iloc
print('range(len(df)) + iloc')
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3])
print()

# df.index
print('df.index')
for i in df.index:
    print(df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3])
print()

# iterrows()
print('iterrows()')
for (idx, col) in df.iterrows():
    print(col[0], col[1], col[2], col[3])
print()

print('1. {키: [리스트]} 형태의 딕셔너리로 dataframe 생성')
raw_data = {'open': [11650, 11100, 11200, 11100, 11000],
            'high': [12100, 11800, 11050, 11100, 11150],
            'low': [11600, 11050, 10900, 10950, 10900],
            'close': [11900, 11600, 11000, 11100, 11050]}

raw_date = pd.DataFrame(raw_data)

print('3. 날짜를 행(row) 인덱스로 설정하고 컬럼명도 별도로 설정')
date = ['20.02.29', '20.02.26', '20.02.25', '20.02.24', '20.02.23']
df = pd.DataFrame(raw_data,
                  columns=['open', 'high', 'low', 'close'],
                  index=date)
print(df)

print("5. 시가(open) 컬럼만 조회")
print(df['open'])
print()

print("6. 고가(high) 컬럼만 조회")
print(df.high)
print()

## 행 접근하기
print("7. 0 ~ 1 번 째 행 조회[2번 째 행은 미포함]")
print(df[0:2])
print()

print("7.1 loc를 이용하여 한 행 조회")
print(df.loc['20.02.29'])
print()

print("8. 20.02.29 ~ 20.02.26 행 조회")
print(df.loc['20.02.29' : '20.02.26'])
print()

print("9. 행과 열로 조회")
print(df.loc['20.02.29' : '20.02.25', ['open', 'high']])

print("10. 모든 행과 열로 조회")
print(df.loc[:, ['open', 'high', 'low', 'close']])

print("11. 스칼라 값(값 한개 조회)")
print(df.loc[date[0], 'high'])

print('12. 위치로 조회 0 번 째 로우 인덱스 모든 값 df.iloc[0]')
print(df.iloc[0])

print('13. 위치로 조회 0번째 ~ 3직전까지의 로우 인덱스 모든값')
print(df.iloc[0:3])
print()

print('14. 위치로 조회 로우 인덱스 0 ~ 3, 컬럼 인덱스 0~2의  모든값')
print(df.iloc[0:3, 0:2])
print()

print('15. 위치로 조회 로우 인덱스 0, 2, 3 컬럼 인덱스 0,2,3')
print(df.iloc[[0, 2, 3], [0, 2, 3]])
print()

print('16. _get_value(행인덱스명, 컬럼명)')
for i in df.index:
    print(i, df._get_value(i, 'open'), df._get_value(i, 'high'), df._get_value(i, 'low'), df._get_value(i, 'close'))
print()

print('17. 값에 대한 빠른 접근')
print(df.iat[1,2])

print('18. bool 필터링 - 시가가 11650 보다 작은 데이터 모두 조회')
print(df[df['open'] < 11650])
print()

print('19. bool 필터링 - 전체 값 중에서 11250보다 큰 값')
print(df[df > 11250])
print()

print('19.1 복합조건 필터링')
print(df[(df >= 11600) & (df <= 11800)])
print()

print("20. at['20.02.29', 'open]")
df.at['20.02.29', 'open'] = 11950
print(df)

print("21. iat[0, 1)")
df.iat[0, 1] = 11850
print(df)

print("22. 정렬, 날짜 오름차순 정렬")
print(df.sort_index(axis=0,ascending=True))
print()

print("22.1 정렬, 날짜 내림차순 정렬")
print(df.sort_index(axis=0,ascending=False))
print()

print('23. 특정 열 이름(open)으로 내림차순 정렬')
print(df.sort_values(by='open', ascending=False))
print()

print('24. 특정 열 이름 여러개로 정렬')
print(df.sort_values(by=['open', 'high'], ascending=False))
print()

print('25. 행과 열 바꾸기, T속성')
print(df.T)
print()

print("26. 전체 행 인덱스")
print(df.index)
print()
print("27. 전체 칼럼 인덱스")
print(df.columns)
print()
print("28. dataFrame(행 x 열) 모습")
print(df.shape)