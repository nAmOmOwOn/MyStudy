distance = 0 # 잘보이는 거리 단위 : cm
def diopter(distance):
    diopter = 0
    if distance < 10 :
        diopter = "-10이상입니다."
    elif distance > 10 and distance < 15 :
        diopter = "-8 ~ -10"
    elif distance > 15 and distance < 20 :
        diopter = "-5 ~ -8"
    elif distance > 20 and distance < 33 :
        diopter = "-3 ~ -5"
    elif distance > 33 and distance < 50 :
        diopter = "-2 ~ -3"
    elif distance > 50 and distance < 100:
        diopter = "-1 ~ -2"
    elif distance > 100 :
        diopter = "-1 이하"
    return diopter
    
def hyperdiopter(distance):
    if distance == "Far blur and Near blur":
        return "Hyperopia Eyes"



