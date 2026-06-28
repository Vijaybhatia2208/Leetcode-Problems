def method1(n):
    # TC = 32
    count = 0
    for i in range(0, 32):
        if n & 1<< i:
            count+=1
    print(count)

def method2(n):
    # TC = log(n)
    count = 0
    i = 0
    while n > 0:
        if n& 1 > 0:
            count+=1
        n= n>>1
    
    print(count)
    


method1(64)
method1(31)
method1(25)

