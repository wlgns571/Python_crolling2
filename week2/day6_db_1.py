import cx_Oracle
conn = cx_Oracle.connect('study', 'study', 'localhost:1521/XE')
name = input("이름을 입력해주세요?: ")
memberList = []
meminfo = []
# 리턴할 배열
with conn:
    # cursor는 휘발성
    cur = conn.cursor()
    sql = """ select *
              from member
              where mem_name like '%'||:word||'%'
    """
    rows = cur.execute(sql, {'word': name})
    columns = [d[0] for d in rows.description]
    for i in rows:
        memberList.append(i)

    for i in range(len(memberList)):
        meminfo.append([(memberList[i])[0], (memberList[i])[12], (memberList[i])[13], (memberList[i])[17]])



print(type(memberList[0]))
# 튜플
print((memberList[0])[0])
#a001

# meminfo.append((memberList[0])[0])
# meminfo.append((memberList[0])[12])
# meminfo.append((memberList[0])[13])
# meminfo.append((memberList[0])[17])
print(memberList)

print('meminfo == ',meminfo)


# 터미널에서 고객 이름을 입력 받아 아이디, 이메일, 직업, 마일리지 리턴 함수 작성