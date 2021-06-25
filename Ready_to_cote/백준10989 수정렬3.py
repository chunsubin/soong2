import sys

n=int(input())
cnt=[0]*10001

for i in range(n):
    t=int(sys.stdin.readline())
    cnt[t]+=1

for i in range(1,len(cnt)):
    if cnt[i]!=0:
        for j in range(cnt[i]):
            print(i,end=" ")