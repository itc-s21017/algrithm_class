MAX = 6
que = [0] * MAX
head = 0
tail = 0
def enqueue(d):
    global tail
    nt = (tail + 1) % MAX

    if nt == head:
        print("これ以上データを入れられません")
    else:
        que[tail] = d
        tail = nt
        print(d + 1,"人待ちに入ります")
        print("待ち時間", d * 15 + 15, "分です")
def dequeue():
    global head
    if head == tail:
        print("取り出すデータがない")
        return None
    else:
        d = que[head]
        head = (head + 1) % MAX
        return d

for i in range(6):
    enqueue(i)
for i in range(6):
    d = dequeue()


