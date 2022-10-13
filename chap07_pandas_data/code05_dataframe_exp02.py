
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

## 데이터 조작(수정/대체)
# replace() : 특정 값을 대체
# 1. df = df.replace(기존값, 변경값)
# 2. df = df.replace({'열 이름' : 기존값}, 변경 값)## 데이터 조작(수정/대체)
# replace() : 특정 값을 대체
# 1. 사용방법 : df = df.replace(기존값, 변경값)
# 2. 사용방법 : df = df.replace({'열 이름' : 기존값}, 변경 값)
a={'A' :[1,2,3,4,5,6],
   'B' : [10,20,30,40,50,60],
   'C' : [100,200,300,400,500,600]}
df = pd.DataFrame(a)
df = df.replace(500,555)
df = df.replace({'B:50'},55)
print('14. replace() 함수 값 변경',df)

## 데이터 구조 변경
# pivot() : 여러 분류로 섞인(중복) 행 데이터를 열 데이터로 회전시키는 기능
'''
pivot(index='', columns='', values='')
    index : 데이터프레임의 index로 사용될 컬럼
    columns : 데이터프레임의 컬럼명으로 사용될 컬럼
    values : 데이터프레임의 데이터로 사용될 컬럼
'''

# 아래 데이터프레임을 보면 동일한 상품이 서로 다른 행에 중복하여 두고 있어 자료를 찾기 쉽지 않다.
# 인덱스를 item으로 하고 type을 열의 레이블로 하여 데이터 프레임을 변경
df_1 = pd.DataFrame({'item' : ['ring0', 'ring0', 'ring1', 'ring1'],
                     'type' : ['gold', 'silver', 'gold', 'bronze'],
                     'price' : [20000, 10000, 50000, 30000]})

df_2 = df_1.pivot(index='item', columns='type', values='price')

print('15. pivot() 적용 안된 df_1 : ')
print(df_1)
print()

print('15. pivot() 적용된 df_2 : ')
print(df_2)
print()

# pivot() 함수 2
df_3 = pd.DataFrame([
    ['20180901', 'A', 10],
    ['20180901', 'B', 100],
    ['20180901', 'C', 1000],
    ['20180902', 'A', 20],
    ['20180902', 'B', 200],
    ['20180902', 'C', 2000],
    ['20180903', 'A', 30],
    ['20180903', 'B', 300],
    ['20180903', 'C', 3000]], columns= ['date', 'type', 'volume'])
print('16. pivot() 적용전 raw df_3 : ')
print(df_3, '\n')

pivot_df = df_3.pivot(index='date', columns='type', values='volume')
pivot_df.columns = pivot_df.columns.values
pivot_df.reset_index(level=0, inplace=True)
print('16.1 pivot() 적용된 pivot_df : ')
print(pivot_df)

## 데이터 프레임 합치기(연결)
# concat([데이터프레임, 데이터프레임])
df_1 = pd.DataFrame({
    'A' : ['a10', 'a11', 'a12'],
    'B' : ['b10', 'b11', 'b12'],
    'C' : ['c10', 'c11', 'c12']}, index=['가', '나', '다']
)

df_2 = pd.DataFrame({
    'B' : ['b23', 'b24', 'b25'],
    'C' : ['c23', 'c24', 'c25'],
    'D' : ['d23', 'd24', 'd25']}, index=['다', '라', '마']
)

concat_df1 = pd.concat([df_1, df_2])
print('17. pd.concat([df_1, df_2]) 작용된 concat_df1 : \n', concat_df1, '\n')

# 결측치 제거(행 전체 제거, 열만 제거)
'''
    # 행의 데이터 중에 하나라도 결측치가 발견되면
    # 해당 행을 삭제하고 기존 데이터 프레임 수정
    
    dropna(axis=0, how='any', inplace=False)
        axis : 0일 경우, 결측치를 포함한 행을 삭제
             : 1일 경우, 결측치를 포함한 열을 삭제
             
        how  : any 일 경우, 결측치가 하나라도 포함되고 있으면 제거 대상
             : all 일 경우, 행 또는 열의 모든 데이터가 결측치일 때만 제거 대상
        
        inplace : True 일 경우, 원본 데이터에서 결측치를 제거
                : False일 경우, 원본 데이터는 그대로 유지하고, 수정된 데이터만 데이터프레임으로 반환
'''

filePath = "/Users/tuan/Documents/pythonWorks/weather.csv"
weather_df = pd.read_csv(filePath, encoding="CP949")
missing_data = weather_df[weather_df['평균풍속'].isna()]
print('30. 평균 풍속이 NaN인 데이터만 선별, Missing_data \n', missing_data, '\n')
weather_df.dropna(axis=0, how='any', inplace=True)
print('31. weather_df : loc[559]')
print(weather_df)

## [sort 추가] 정렬
# sort_values(column_list, ascending="False", inplace=False)
#   column_list : 컬럼명 리스트(예 : [컬럼명, 컬럼명])
#   ascending : 정렬 방식 (True/False)
#   inplace : 기존 데이터 프레임에 수정 적용 여부 (True/False)

filePath = "/Users/tuan/Documents/pythonWorks/countries.csv"
countries_df = pd.read_csv(filePath, index_col=0)

print("32. 인구와 지역으로 역정렬, 원본 df에 미반영 \n")
sort_df_two_column = countries_df.sort_values(by=['population', 'area'],
                                              ascending= False,
                                              inplace= False)
print(sort_df_two_column, '\n')
print(countries_df)
