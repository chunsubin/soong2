inp = int(input())
a = 666
number = "666"
cnt = 1
if inp == 1:
    print(666)

else:
    for i in range(10000000):
        a = a + 1
        if number in (str(a)):
            cnt += 1

        if inp == cnt:
            break

    print(a)