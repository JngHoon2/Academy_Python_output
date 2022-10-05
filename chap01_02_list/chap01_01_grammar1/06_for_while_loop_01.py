if __name__ =='__main__':

    # for i in range(0,3, 1):
    #     print("for문")
    #
    # hap = 0
    # for i in range(1, 11, 1):
    #     hap = hap +i
    #     print(hap)
    #
    # #break 반복문을 빠져나가 더이상 반복작업 안함
    # hap, i=0,0
    # for i in range(1,101):
    #     hap += i
    #     if hap >=1000:
    #         break
    # print("1~100의 합계중 누적해서 1000이 넘게하는 숫자는 %d"%i)
    #
    # #continue : for 문으로 돌아가서 계속 반복작업
    # hap, i = 0, 0
    # for i in range(1, 101):
    #     if i%3==0:
    #         continue
    #     hap +=i
    # print(hap)
    #
    # sum=0
    # for n in range(1,101):
    #     if n%5==0:
    #         sum +=n
    # print("5의 배수의 합 : ",sum)
    #가로로 출력
    for num in range(0,10):
        # print(num)
        print(num ,end="\t")

    # # 2022년 01~12월 출력
    # month=1
    # while month <=12:
    # print(f'2022년 {month}월')
    # month +=1

    # x,y=1,1
    # for a in range(1,10):
    #     # print(end="\n")
    #     for b in range(1,10):
    #         print("%d * %d : %d"%(b,a,b*a),end="\t")
    #     print()

    for a in range(1,10):
        print(end="\n")
        for b in range(1,10):
            print("%d * %d : %d"%(b,a,b*a),end="\t")
