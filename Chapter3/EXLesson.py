import queue

Max = 10

print("キュー")
q = queue.Queue()
for i in range(Max):
    q.put(i)
for i in range(Max):
    print(q.get(), end="→")

print("\n")
print("スタック")
s = queue.LifoQueue()
for i in range(Max):
    s.put(i)
for i in range(Max):
    print(s.get(), end="→")