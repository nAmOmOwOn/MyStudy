age = 0

def firstage(age):
    addition = 0
    if age < 40 and age > 35 :
       addition += 0.5
       return addition

def secondage(age):
    addition = 0
    if age > 40 and age < 45 :
       addition += 1.0
       return addition

def thirdage(age):
    addition = 0
    if age > 45 and age < 50 :
       addition += 1.25
       return addition
    
def forthage(age):
    addition = 0
    if age > 50 and age < 55 :
       addition += 1.75
       return addition

def fifthage(age):
    addition = 0
    if age > 55 and age < 60 :
       addition += 2.25
       return addition
    
def sixthage(age):
    addition = 0
    if age > 60 :
       addition += 2.75
       return addition