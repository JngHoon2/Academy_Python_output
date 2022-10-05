if __name__ == '__main__':
    lan = int(input("국어점수을 입력하세요 : "))
    eng = int(input("영어점수을 입력하세요 : "))
    mat = int(input("수학점수을 입력하세요 : "))

    sum=lan+eng+mat
    print(sum)

    avg=sum/3
    print('점수의 평균은 {0:0.2f}'.format(avg))



