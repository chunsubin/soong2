first, second = map(int,input().split())
for i in range(first, second+1):
    cnt=0
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
            if cnt==2:continue

    print(i)