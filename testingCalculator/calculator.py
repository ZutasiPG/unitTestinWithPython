import math
def osszeadas(a,b):
    return a+b
def kivonas(a,b):
    return a-b
def szorzas(a,b):
    return a*b
def osztas(a,b):
    if b==0:
        return "Hiba: nullával való osztás!"
    return a/b  
def gyok(a):
    if a<0:
        return "Hiba: negatív számnak nincs valós gyöke!"
    return math.sqrt(a)
