import math
king = [1,1,2,2,2,8]

inp = list(map(int,input().split()))

for i in range(6):
    print(int(king[i]-inp[i]),end=" ")