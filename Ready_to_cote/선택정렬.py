arr=[]

size = int(input())
for i in range(size):
    arr.append(int(input()))

for i in range(size-1):
    min=i
    for j in range(i+1,size):
        if arr[j]<arr[min] :
            min=j

    arr[min],arr[i]=arr[i],arr[min]

print(arr)