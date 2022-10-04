
# [연습문제]
# 국어 영어 수학 3과목의 점수를 입력받고
# 합계와 평균을 구하시오.
import math

if __name__ == "__main__":
    korean = input("국어 점수 : ")
    english = input("영어 점수 : ")
    math = input("수학 점수 : ")

    sum = int(korean) + int(english) + int(math)

    print("3과목 합계 : {0}".format(sum))
    print("3과목 평균 : {0}".format(round(sum / 3, 2)))
