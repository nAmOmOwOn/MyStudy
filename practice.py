class Rabbit :
    shape = ""
    xPos = 0
    yPos = 0

    def __init__(self, value):
        self.shape = value

    def goto(self, x, y):
        self.xPos = x
        self.yPos = y

rabbit = Rabbit("원")

print(rabbit.shape)