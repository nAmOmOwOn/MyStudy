'''
파일명 : Ex16-2-destructor.py
소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.
'''
class Service:

    def __init__(self, service=None):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))
        
    def __del__(self): # 메모리에서 지워지기 전에 호출되는 메소드(함수)
        print('{} Service가 종료되었습니다.'.format(self.service))

s = Service('길 안내')
del(s) # == del s 이렇게 입력해도 됨


s2 = Service()

print("프로그램 종료!")