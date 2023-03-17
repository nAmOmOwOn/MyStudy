'''
파일명 : Ex14-4-csvQuoteReader.py
'''
member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        '''
           ["강나라",필라테스,25일\n]
        '''
        member[0] = member[0].strip('"')
        member[2] = member[2].strip('\n')
        '''
           [강나라,필라테스,25일]
        '''
        member_list.append(member)

print(member_list)
