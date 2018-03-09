words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

# 使用数组访问操作符，能够迅速地生成数组的副本
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

# words -> ['defenestrate', 'cat', 'window', 'defenestrate']

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])