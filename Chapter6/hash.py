def hash(key):
    h = 0
    for i in key:
        if i != " ":
            h = h + ord(i)
    return (h%1000)
print("文字列を入力してください")
print("何も入力しないと終了します")
while True:
    s = input("文字列を入力してください")
    if s == "":
        break
    print(s, "→ハッシュ値", hash(s))
#濱村悠 →ハッシュ値 842