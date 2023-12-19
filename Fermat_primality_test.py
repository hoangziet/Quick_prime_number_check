from random import randint

def binPow(n,e,m):
    if e == 0 : return 1
    if e % 2 == 0 : return binPow(n**2%m,e//2,m)
    if e % 2 == 1 : return n*binPow(n**2%m,e//2,m)%m
    
def FermatCheck(n):
    if n<4 : return n==2 or n==3 
    for i in range(5):
        rd = randint(2,n-1) 
        if binPow(rd,n-1,n) != 1 :
            return False
    return True

# print(FermatCheck(12323))
