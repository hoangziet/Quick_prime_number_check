n = 100
isPrime = [1]*n
isPrime[0]=0
isPrime[1]=0
for i in range(2,n):
    if isPrime[i] == 1 : 
        j = 2*i 
        while j < n :
            isPrime[j] = 0
            j += i

res = []
for i in range(n):
    if isPrime[i]==1 :
        res.append(i)
        
# print(res)