
if __name__ == '__main__':
    name_list = ['일순이', '이돌이', '삼순이', '사돌이', '오돌이', '육순이', '칠순이', '팔돌이']
    pay_list = [460, 280, 360, 270, 300, 550, 600, 720]
    gender_list = ['F', 'M', 'F', 'M', 'M', 'F', 'F', 'M']
    country_list = ['US', 'FR', 'KR', 'DE', 'AU', 'JP', 'KR', 'KR']

    #[1] 인덱스를 사용하여 이름을 출력하시오.
    for i in range(len(name_list)):
        print(name_list[i])

    #[2] 급여가 360 이상인 사원수 출력

    cnt = 0
    for i in range(len(pay_list)):
        if pay_list[i] >= 360:
            cnt += 1
    print('급여가 360 이상인 사원수 : {0}'.format(cnt))
    print()

    #[3] 남자 사원들의 이름과 인원 수

    male_cnt = 0;
    for i in range(len(gender_list)):
        if gender_list[i] == 'M':
            print(name_list[i], ' ', end='')
            male_cnt += 1
    print()
    print('남자 사원의 인원 수 : {0}'.format(male_cnt))
    print()

    #[4] 남자 사원들의 이름과 국적을 출력하시오.
    for i, gender in enumerate(gender_list):
        if gender == 'M':
            print('{0} 사원의 국적 : {1}'.format(name_list[i], country_list[i]))
    print()

    #[5] 여사원들의 이름, 급여합계, 총인원수는?
    sum = 0;
    female_cnt = 0
    for i, gender in enumerate(gender_list):
        if gender == 'F':
            print(name_list[i], ' ', end='')
            sum += pay_list[i]
            female_cnt += 1
    print()
    print('여사원들의 급여합계는 {0}만원이고, 총인원수는 {1}명입니다,'.format(sum, female_cnt))
    print()

    #[6] 한국에서 근무하는 여사원들의 인원수와 평균 급여는?
    kr_female_cnt = 0
    sum2 = 0;
    for i, gender in enumerate(gender_list):
        if gender == 'F':
            if country_list[i] == 'KR':
                sum2 += pay_list[i]
                kr_female_cnt += 1
    print('한국에서 근무하는 여사원들의 인원수는 {0}명이고, 평균급여는{1}입니다.'.format(kr_female_cnt, sum2/kr_female_cnt))
