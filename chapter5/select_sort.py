data = ["こうた", "しゅんた", "こうま", "あさひ", "ゆう", "りゅうき", "よしや", "ゆきたか", "せいか", "きょうすけ"]

print(data, "元のデータ")

for i in range(0, 9):
    m = i
    for j in range(i+1, 10):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, "ソート後のデータ")