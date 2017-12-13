animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.


animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line


nums = list(range(1,5))    # range is a built-in function that creates a list of integers
print(nums)         # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])     # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])      # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print(nums[:-1])    # Slice indices can be negative; prints ["0, 1, 2, 3]"
nums[2:4] = [8, 9] # Assign a new sublist to a slice
print(nums)         # Prints "[0, 1, 8, 9, 4]"


#循环遍历

#for-in 可以用来遍历数组与字典：

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

# 使用数组访问操作符，能够迅速地生成数组的副本
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

# words -> ['defenestrate', 'cat', 'window', 'defenestrate']
#如果我们希望使用数字序列进行遍历，可以使用 Python 内置的 range 函数：

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


#Python 字符串支持分片、模板字符串等常见操作:

var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
# var1[0]:  H
# var2[1:5]:  ytho

print("My name is %s and weight is %d kg!" % ('Zara', 21))
# My name is Zara and weight is 21 kg!
var1[0:4]
len(str)

string.replace("-", " ")
",".join(list)
"hi {0}".format('j')
str.find(",")
str.index(",")   # same, but raises IndexError
str.count(",")
str.split(",")

str.lower()
str.upper()
str.title()

str.lstrip()
str.rstrip()
str.strip()

str.islower()
# 移除所有的特殊字符
re.sub('[^A-Za-z0-9]+', '', mystring)
#如果需要判断是否包含某个子字符串，或者搜索某个字符串的下标:

# in 操作符可以判断字符串
if "blah" not in somestring: 
    print('suc')

# find 可以搜索下标
s = "This be a string"
if s.find("is") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")
