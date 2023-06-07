LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "38.5℃以上の発熱がある？"],
    [3, 4, "元気がある？"],
    [5, 6, "胸がひいひい？"],
    [None, None, "氷枕で病院"],
    [None, None, "様子を見る"],
    [None, None, "解熱剤で病院"],
    [None, None, "速攻で病院"]
]

n = 0
while node[n][LEFT] and node[n][RIGHT]:
    reply = input(f'{node[n][DATA]}(y or n):')
    if reply == "y":
        n = node[n][RIGHT]
    elif reply == "n":
        n = node[n][LEFT]
print(f'結果　{node[n][DATA]}')