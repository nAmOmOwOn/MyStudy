class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyalbe:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyalbe, Unit):
    def __init__(self):
        super().__init__()


dropship = FlyableUnit()