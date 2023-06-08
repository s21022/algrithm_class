data = ["こうた", "しゅんた", "こうま", "あさひ", "りゅうき", "よしや", "ゆきたか", "せいか", "せいが", "きょうすけ"]

print(data, "元のデータ")

for i in range(0, 9):
    m = i
    for j in range(i+1, 10):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, "ソート後のデータ")