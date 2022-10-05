if __name__ == '__main__':
    f=float(input("온도를 입력하세요 : "))
    c=(f-32)*(5/9)

    print("화씨온도는 {0:0.2f}, 섭씨온도는 {1:0.2f}".format(f,c))