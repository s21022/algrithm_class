data = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]
node = ["沖縄", "奈良", "大阪", "千葉", "東京"]

for y in range(5):
    for x in range(y, 5):
        if data[y][x]==1 and data[x][y]==1:
            print(node[y]+"<->"+node[x])