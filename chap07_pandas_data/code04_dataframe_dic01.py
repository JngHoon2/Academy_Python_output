
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