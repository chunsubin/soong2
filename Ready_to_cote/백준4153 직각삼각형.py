import sys
while(True):
    inp=sys.stdin.readline()
    number = list(map(int, inp.split()))
    if number[0]== 0:break
    number.sort()
    if number[0]*number[0]+number[1]*number[1]==number[2]*number[2]:
        print("right")
    else:
        print("wrong")