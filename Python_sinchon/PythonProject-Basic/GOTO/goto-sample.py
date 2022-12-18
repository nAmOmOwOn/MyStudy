'''
Goto 모듈 테스트
python 3.6 버전까지 테스트성공

모듈 설치
pip3 install goto-statement


파이참 label goto 명령어 빨간줄 에러표시 무시하고 사용가능!
'''

from goto import with_goto
print('Goto Test')

@with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    print('begin')
    if i == stop:

        goto .end

    result.append(i)
    i += 1
    goto .begin


    label .end
    print('end')
    print(i)
    return result

range(1, 4)