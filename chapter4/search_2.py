data = [57, 48, 44, 32, 18, 484, 82, 60, 4, 11]
n = len(data)
key = 60
i = 0
while i < n and data[i] != key:
    i += 1
if i == n:
    print(str(key) + "は存在しない")
else:
    print("data[{}]が{}です。".format(i, key))