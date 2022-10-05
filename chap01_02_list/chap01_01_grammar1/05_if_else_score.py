if __name__ == '__main__':
    # 주석을 해제하면서 테스트 하세요
    #if else 문
    # a=230
    # if a>200:
    #     print('200보다 큽니다')
    # else:
    #     print('200보다 작습니다.')

    #점수로 성적레벨 조회함수
    def print_score(score):
        if score>=95:
            grade="A+"
        elif score>90:
            grade="A0"
        elif score > 90:
            grade = "A0"
        elif score > 85:
            grade = "B+"
        elif score > 80:
            grade = "B0"
        elif score > 75:
            grade = "C+"
        elif score > 70:
            grade = "C0"
        elif score > 65:
            grade = "D+"
        elif score > 60:
            grade = "D0"
        else:
            grade="F"
        return grade

    def exist_friut(fruit):
        fruit_list=['딸기','사과','배','오렌지','바나나','파인애플']
        if fruit in fruit_list:
            print('{0}은 과일 목록에 존재합니다'.format(fruit))
        else:
            print('{0}은 과일목록에 존재하지 않습니다.'.format(fruit))




    score=int(input("점수를 입력하세요 : "))
    grade=print_score(score)
    print("등급은 : ",grade)

    fruit=input('과일을 입력하세요 : ')
    exist_friut(fruit)