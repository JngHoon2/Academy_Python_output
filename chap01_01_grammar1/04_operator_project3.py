
if __name__ == "__main__" :
    f = input("화씨 온도를 입력하세요 : ")
    print("섭씨 온도는 {0}입니다.".format(round((int(f) - 32) * (5/9), 2)))