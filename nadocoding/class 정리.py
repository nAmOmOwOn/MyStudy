# 클래스는 붕어빵 틀 같은 존재!!

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(name))
        print("체력 {0} 데미지{1} 입니다".format(hp,damage))

marine1 = Unit("마린" , 40, 5)