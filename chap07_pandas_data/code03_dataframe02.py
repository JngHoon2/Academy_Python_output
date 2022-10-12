
import pandas as pd
import numpy as np

# 일자별 온라인 + 오프라인 판매금액 관련 dataframe 예제
dates = ['10/01','10/02','10/03','10/04','10/05','10/06']
online_sales = [300, 280, 350, 650, 500, 450]
offline_sales = [150, 130, 210, 130, 100, 200]

# 날짜(dates)를 인덱스로 하여 데이터프레임 생성
df = pd.DataFrame({"on_sales" : online_sales,
                   "off_sales" : offline_sales},
                  index=dates)
print(df)
print()

# df.iterrows() 함수로 행 반복
# 각 행별로 idx('10/01')와 col(Series)를 반복
# 열 시리즈에 [인덱스 순번]으로 접슨
# iterrows()는 각 행을 시리즈 형태로 반복하기 때문에 가장 느림
print('13. 열 시리즈에 [인덱스 순번]으로 접근')
for idx, col in df.iterrows():
    print(idx, col, col[1]) # col은 series이므로 정수로 접근 가능
print()

print('14. 열 series에 컬럼 인덱스 이름으로 접근')
for idx, col in df.iterrows():
    print(idx, col['on_sales'], col['off_sales'])
print()

# 열 series에 대괄호[] 없이 점(.)찍고 컬럼 인덱스 이름으로 접근
print('15. 열 series에 대괄호[] 없이 점(.)찍고 컬럼 인덱스 이름으로 접근')
for idx, col in df.iterrows():
    print(idx, col.on_sales, col.off_sales) #행의 이름으로도 접근 가능
print()

print('16. loc[행인덱스이름, 열인덱스이름]으로 접근 가능')
for i in df.index:
    print(i, df.loc[i, 'on_sales'], df.loc[i, 'off_sales'],
          df.loc[i, 'on_sales'] + df.loc[i, 'off_sales'])

print('17. loc[행인덱스이름, 열인덱스이름]으로 접근 가능')
for i in df.index:
    print(i, df.loc[i][0], df.loc[i][1], df.loc[i][0] + df.loc[i][1])

print('18.1 df.itertuples()로 행 반복하고 row[0]로 접근')
for row in df.itertuples():
    print(row, row[0], row[1], row[2], row[1] + row[2])
print()

print('19. range(len(df)) 행 반복 = df.iloc[0,0]으로 접근')
for i in range(len(df)):
    # type(df.iloc[i]) : Series
    print(i, df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 1] + df.iloc[i, 1])
print()