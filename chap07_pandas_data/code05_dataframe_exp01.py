### 파이썬에서 CSV 핸들링
# 파이썬이 제공하는 CSV 모듈
import csv
import pandas as pd

filePath = "/Users/tuan/Documents/pythonWorks/countries.csv"
#pd.read_csv() : 첫번 째 인자는 경로, index_col에 0을 넘겨주면 0번 째 열이 인덱스로 사용
contries_df = pd.read_csv(filePath, index_col=0)
print(contries_df)
print()

# 국가 컬럼만 조회

print("1. 국가 컬럼만 조회")
print(contries_df['country'])
print()

print("2. 행 인덱스가 KR인 행 조회 loc()")
print(contries_df.loc['KR'])
print()

print("2.1 한국의 인구 스칼라 값")
print(contries_df.iat[0,3])
print()

#dataframe에서 상위 5개 행 조회
print("3. dataframe에서 상위 5개 행 조회")
print(contries_df.head())
print()