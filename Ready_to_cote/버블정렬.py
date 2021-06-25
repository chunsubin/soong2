arr=[]

size = int(input())
for i in range(size):
    arr.append(int(input()))

for i in range(size-1,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)