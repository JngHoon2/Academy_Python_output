###파이썬 데이터 타입[자료형]

#데이터 타입
#1. 숫자형으로 정수형과 실수형이 있다.
#2. 그외 기본형으로 블형, 문자형이 있으며 확장형인 리스트,튜플, 딕셔너리, 집합 등이 있다.
#변수 선언/초기화 부분(값이 할당되면서 자료형이 결정됨)
bool_var= True
int_val = 0
_float_val = 3.14
str_val = 'Hello World'

#스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print(bool_var,int_val,_float_val,str_val)
    print(type(int_val)) # typr()함수를 통해서 변수의 자료형을 알 수 있다
    print(type(str_val)) # class 'str'로 표시된다. 문자열형임을 표시