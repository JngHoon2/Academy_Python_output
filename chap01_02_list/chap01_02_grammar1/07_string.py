if __name__ =='__main__':

    jumin="981130-1234567"
    #[1] 문자열 인덱싱
    # print('-----------인덱싱-----------------')
    # print(jumin[0])
    # print(jumin[1])
    # print(jumin[-1])
    # print(jumin[-2])
    #
    # if jumin[7]=='1':
    #     print("남성")
    # else:
    #     print("여성")
    #
    # print('-----------문자열 인덱싱 반복------------')
    # for a in range(0,len(jumin)):
    #     a=jumin[a]
    #     print(a, end="")
    # print()
    # #------
    # for a in jumin:
    #     print(a,end="")
    # print()
    # # while문으로 반복
    # i=0
    # while i < len(jumin):
    #     print(jumin[i],end="")
    #     i+=1

    kor= 'Beautiful Korea'
    print("------그외 문자열 조작 함수----------")
    print(kor.upper())
    print(kor.lower())
    print(kor[0].isupper())
    print('{0}의 문자열 개수는 {1}'.format(kor,len(kor)))
    print()

    #문자열 대체 repalce()
    print(kor.replace('Beautiful','Strong'))

    idx=kor.index('K')
    print('index k : ',idx)
    print(kor[idx:])

    #find()함수
    print('find()함수로 찾은 K인덱스',kor.find('K'))
    #검색 결과 같은 단어가 없으면 -1리턴
    print('find()함수로 찾은 People인덱스',kor.find('People'))
    #검색 결과 같은 단어가 없으면 오류[find와 차이점]
    print('index() 함수로 찾은 People인덱스',kor.index('Korea'))