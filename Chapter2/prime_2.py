p = [True]*90
p[0] = False
p[1] = False
n = 2

def hyou():
    s = ""
    count = 0
    for i in range(82):
        if p [i] == True:
            s += "{:2d}, ".format(i)
            count += 1
        else:
            s +="/,"
        if i%10 == 9:
            s += "\n"
    print(s)
    print("素数は" + str(count) + "個です")
def  furui():
    f = 0
    global n
    for i in range(n+n, 82, n):
        p[i] =False
    print(n, "の倍数を篩い落としました")
    hyou()
    while n < 82:
        n = n + 1
        if p[n] == True:
            break

hyou()
while n < 10:
    input("Enterキーを押してください")
    furui()
