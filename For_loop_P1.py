row = 6
for w in range(1,row+1):
    num=w
    t=row-1
    for a in range(1,w+1):
        print(num,end=" ")
        num+=t
        t-=1
    print("")


