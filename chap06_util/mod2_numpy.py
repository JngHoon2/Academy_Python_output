
# 넘파이(numpy) 라이브러리
# 1. 넘파이는 C언어로 구현된 파이썬 라이브러리로써, 고성능의 수치 계산을 위해 제작되었다.
# 2. Numerical Python의 약자로 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공한다.
# 3. 데이터 분석을 할 때 사용되는 하이브러리인 pandas와 matplotlib의 기반으로 사용된다.
# 4. 넘파이에서는 기본적으로 array라는 단위로 데이터를 관리하며 이에 대해 연산을 수행한다.
# 5. 일반 List에 비해 빠르고, 메모리를 효율적으로 사용한다.

import numpy as np

data1 = [1,2,3,4,5]
arr2 = np.array([1,2,3,4,5])
print(arr2, type(arr2))

print("1. 넘파이 배열의 형태(shap) : ", arr2.shape)
print("2. 넘파이 배열의 자료형 : ", arr2.dtype)

arr3 = np.array([[1,2,3],
                 [4,5,6]])

arr4 = np.array([[7,8,9],
                 [10,11,12]])

print("3. 넘파이 배열 간 합계 : ", arr3 + arr4)

arr5 = np.array([2,3,4])

print("4. 형태가 다른 배열 간 연산 : ", arr3 + arr5)


arr6 = np.arange(10)
print("5. arr6", arr6)
print()

print("6. 슬라이싱 arr6[3:5] : ", arr6[3:5])

arr7 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
print("7. 2차원 배열 인덱싱 arr7[2,3] : ", arr7[2,3])
print("8. arr7[:, 3]", arr7[:, 3])

data = np.random.randn(2,3)

sum1 = np.sum(arr7)
print("9. 전체 성분의 합 : ", sum1)

sum2 = np.sum(arr7, axis=1)
print("10. sum2 : ", sum2)

sum3 = np.sum(arr7, axis=0)
print("11. sum3 : ", sum3)

avg1 = np.mean(arr7)
print("12. 전체 성분의 평균 : ", avg1)

avg2 = np.mean(arr7, axis=0)
print("13. 행간의 평균 : ", avg2)

min = np.min(arr7)
print("전체에서 최소값 : ", min)

min1 = np.min(arr7, axis=1)
print("행간 최소값 : ", min1)

min_index = np.argmin(arr7)
print("전체에서 최소값의 위치 : ", min_index)

max = np.max(arr7)
print("전체에서 최대값 : ", max)

max_index = np.argmax(arr7)
print("전체에서 최대값의 위치 : ", max_index)

com_sum = np.cumsum(arr7)
print("19. 각 성분 별 누적값 : ", com_sum)

print("20. 순정렬 : ", np.sort(arr7))          # 전체 성분에 대해서 오름차순으로 정렬
print("21. 역정렬 : ", np.sort(arr7)[::-1])    # 전체 성분에 대해서 내림차순으로 정렬

print("22. 행 방향으로 오름차순 정렬 : ", np.sort(arr7, axis=0)) # 행 방향으로 오름차순 정렬

print("23. 2차원 배열 컬럼 축 역정렬 : ", np.sort(arr7, axis=1)[::-1])

print("24. 행 방향으로 오름 파순 정렬 : ", np.sort(arr7, axis=0)) # 행 방향으로 오름차순 정렬