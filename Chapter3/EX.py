Max = 7
node = ["赤", "橙", "黄", "緑", "青", "藍", "紫"]

print("→".join(node))
print("→".join(node[::-1]))

revers = node.range(Max, -1, -1)
print(node[revers])