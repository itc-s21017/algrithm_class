

with open("data.txt", "r", encoding="utf-8") as f:
    data = f.readlines()# 1 行分の文字を読み取り、そのデータを文字列として返すメソッド

new_list = []  # ファイルの内容を展開する配列の宣言
for i in data:#二次元リストとして展開
    word = i.split()
    new_list.append(word)

print(new_list)

a = "田場"
b = "098"
new_list.append([a, b])

with open("data.txt","a") as f:#a:データの追加
    f.write('\n'+a+','+b)#データの整形
