subject = ["国語","算数","英語","理科","社会"]
score = [80, 100, 92, 96, 74]
total = 0
for i in range(5):
    print(subject[i], "の点数は", score[i])
    total += score[i]
print("合計点は", total)
