def factorial(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r
def short(n):
    r=0
    for i in range(1,n+1):
        r+=i
    return r

if __name__=='__main__':
    print('factorial(10)=',factorial(10))
    print('short(10)=',short(10))

#外人分支測試