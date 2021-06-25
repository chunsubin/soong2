arr=[]   # a

size = int(input())
for i in range(size):
    arr.append(int(input()))

length = len(arr)

count = [0]*(length+1)  # 입력받은 arr배열의 숫자 빈도 체크 배열
countSum=[0]*(length+1) # 빈도배열을 통한 누적합 배열

for i in range(0,length):
    count[arr[i]]+=1

countSum[0]=count[0]
for i in range(1,length+1):
    countSum[i]=countSum[i-1]+count[i]

# 최종 정렬된 배열
arr2 = [0]*(length+1)

for i in range(length-1,-1,-1): #거꾸로
    arr2[countSum[arr[i]]]=arr[i]
    countSum[arr[i]]-=1

result=""
for i in range(1,length+1):
    result += str(arr2[i])+" "

print(result)