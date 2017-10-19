#查看元祖
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#遍历元祖
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#重新赋值元祖
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
