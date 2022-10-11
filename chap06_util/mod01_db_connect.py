
 ## 오라클 연동 및 접속 테스트
'''
    cx_Oracle.makedsn : 오라클에 대한 주소 정보
    cx_Oracle.connect : 오라클 접속 유저 정보
    db.cursor : 데이터를 담을 메모리의 이름을 선언
    cursor.execute : SQL의 결과가 cursor 메모리를 담는다
    cursor.fetchall : 메모리에 담긴 데이터를 한 행 씩 fetch 한다. 전부!
    cursor.description : 데이터의 칼럼명을 추출한다.
'''

# import cx_Oracle
# import pandas as pd
#
#
# dsn = cx_Oracle.makedsn('58.148.65.116', 1521, 'orcl')
# db = cx_Oracle.connect('hr2', '1234')
#
# cursor = db.cursor()
# cursor.execute("select * from employees")
#
# row = cursor.fetchall()
# colname = cursor.description
# col = []
#
# for i in colname:
#    col.append(i[0])
#
# # pandas를 사용한 데이터 프레임 형식으로 변환
# emp = pd.DataFrame(row, columns=col)
# print(emp)


import psycopg2

try:
    conn = psycopg2.connect(host = "postgresql.cvzpk8yzjogk.ap-northeast-2.rds.amazonaws.com",
                            dbname="postgres",
                            user="postgres",
                            password="!Aclsrn4242",
                            port=5432)
    cur = conn.cursor()
    cur.execute("select * from hr2.employees")
    rows = cur.fetchall()
    for i in rows:
        print(i)
except psycopg2.DatabaseError as dber:
    print(dber)