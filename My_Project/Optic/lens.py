diopter = 0
Disease = []
lens = ["Lisa", "Lara",  "PanOp", "Vivity", "FineVision", "Synergy", "Lentis"]

def higherMyopia(deopter):
    if deopter < -8:
        return lens[0]
    
def higherHyperopia(deopter):
    if deopter > 8:
        return lens[0]

def haveEyeDisease(Disease):
    if Disease != None:
        return lens[-1]
    
def anotherDiopter(dipoter):
    if dipoter != None:
        return lens