'''
파일명 : Ex14-2-csvReader.py
CSV(comma-separated values)
    필드를 쉼표(,)로 구분한
    텍스트 데이터 파일이다.
'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄 제거
    while True:
        line = file.readline()
        if not line:
            break

            '''
            [
            [10101, 김승별, 서울시 영등포구, 010 - 1111 - 1111]
            ,[10102,박나라,서울시 여의도구,010-2222-2222]
            ...
            ,[10105,이명숙,경기도 과천시,010-5555-5555]
            ]
            
            '''
        student = line.split(',') # ','구분 리스트로 반환
        student_list.append(student) # 리스트 안에 리트스 추가
print(student_list)









