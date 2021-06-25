n= int(input())
cnt=0
for i in range(n,0,-1):
    if n<i*i and n>=(i-1)*(i-1):
        #print(i,i-1)
        n=n-(i-1)*(i-1)
        cnt+=1

print(cnt+n)