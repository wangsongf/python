#使用函数range()
for value in range(1,5):
    print(value)

#使用range() 创建数字列表
numbers = list(range(1,6))
print(numbers)

#even_numbers.py
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares.py
squares = []for value in range(1,11):
	squares.append(value**2)
print(squares)

#对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
