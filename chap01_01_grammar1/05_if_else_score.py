
def print_score(score):
    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A0"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B0"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C0"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D0"
    else:
        grade = "F"
    return grade


def exist_fruit(fruit):
    fruit_list = ['사과', '딸기', '배', '오렌지', '바나나', '파인애플']
    if fruit in fruit_list:
        print("{0}은 과일 목록에 존재합니다.".format(fruit))
    else:
        print("{0}은 과일 목록에 존재하지 않습니다.".format(fruit))

if __name__ == "__main__" :

   #score = input("점수 : ")
   #print("학점 : " + print_score(int(score)))

   fruit = input("과일 : ")
   exist_fruit(fruit)