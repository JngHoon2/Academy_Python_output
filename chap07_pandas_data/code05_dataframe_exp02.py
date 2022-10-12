
import csv
import pandas as pd

filePath = "/Users/tuan/Documents/pythonWorks/weather.csv"

weather_df = pd.read_csv(filePath, encoding="CP949")
print('4. 울릉도 연간 날씨 데이터')
print(weather_df)

# 전체적으로 데이터를 간단하게 분석하여면 describe() 함수 사용
print('5. describe() 함수로 간략한 정보 조회')
print(weather_df.describe())
print()

# 컬럼별 최대값 계산
print('6. 컬럼 별 최대 값 max()')
print(weather_df.max())
print()

max_wind = weather_df['평균풍속'].max()
print('7. 10년간 데이터 중에 평균 풍속 중 가장 높은 값')
print(max_wind)
print()

# groupby 그룹핑
# 같은 값을 하나로 묶어 통계 도는 집계 결과를 얻기 위해 사용
# 데이터를 특정한 값에 기반하여 그룹으로 묶는 방법

print('그룹핑하기')
datetimeIndex = pd.DatetimeIndex(weather_df['일시'])
print('8. 날짜 컬럼만을 선별하여 datetimeIndex 객체로 생성')
print(datetimeIndex)

print('9. DatetimeIndex 객체에서 년/월/일 뽑아내기')
print(datetimeIndex.year)
print(datetimeIndex.month)
print(datetimeIndex.day)
print()

#DatetimeIndex 객체를 활용하여 weather.csv를 분석
# weater.csv 월별로 묶기
# 1. 새로운 열 month를 생성하고 해당하는 달을 기록
# 2. new_df에 month가 같은 값끼리 묶어 평균을 내어 저장

# dataframe 으로 가공
weather_df = pd.read_csv(filePath, encoding='CP949')

# 일시 컬럼에서 월을 그룹핑 하여 추출(중복없이)하여 새로운 컬럼에 할당
weather_df['month'] = pd.DatetimeIndex(weather_df['일시']).month
# 새로운 dataframe을 생성
# weather_df 그룹별 집계연산(sum, count, mean, max, min ...)을 활용
new_df = weather_df.groupby('month').mean()
print('10. 그룹핑한 값에서 컬럼 별 평균 계산')
print(new_df)
print()

# 필터링
# 1. DateFrame에서 단일 조건을 충족하는 행을 갖고 오려면 다음과 같이 입력
#  - DataFrame명[DataFrame명['칼럼명'] == 값 ]
# 2. DataFrame에서 복합 조건을 충족하는 행을 갖고 오려면 다음과 같이 입력
#  - DataFrame명[(DataFrame명['칼럼명1'] == 값) & (DataFrame명['칼럼명2'] == 값)]

#weater.csv에서 초속 10m/s 이상의 강풍이 불었던 날
print('11. 초속 10m/s 이상의 강풍이 불었던 날[필터링]')
print(weather_df[weather_df['최대풍속'] >= 19.0])
print()

# 결측 데이터 처리(결측치)
# 결손값 : 데이터가 수집되지 않았거나 측정 장치의 고장 등으로 데이터를 확보하지 못한 날
# 결손값은 isna() 함수를 이용하여 찾을 수 있다. 결손값은 NaN으로 표기된다.
# NaN : Not a Number의 약자로 숫자 형태의 누락된 데이터 = 결측값을 표현

print('12. 결손값(평균풍속) 찾기 isna() 함수')
print(weather_df[weather_df['평균풍속'].isna()])
print()

# fillna() 함수
# 결측치가 발견되면 지정한 값으로 대체 fillna(대체값, inplace = True)
weather_df.fillna(0, inplace=True)
print('13. 결손값을 fillna() 함수로 채움')
print(weather_df.loc[559])
print()
