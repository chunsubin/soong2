import sys

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
result=""
for i in range(n):
    result += str(arr[i])+" "

print(result)