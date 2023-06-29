date = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
key = int(input("探す値を入力してください "))
left = 0
right = len(date)-1
flg = False

while left <= right:
    mid = (left+right)//2
    print("L={} M={} R={}" .format(left, mid, right))
    if date[mid] == key:
        print("date[{}]が{}です" .format(mid, key))
        flg = True
        break
    if date[mid] < key:
        left = mid + 1
    else:
        right = mid - 1

if flg == False:
    print("その値が見つかりませんでした。")