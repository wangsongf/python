import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
pprint.pprint(stuff)

# 自定义参数
pp = pprint.PrettyPrinter(depth=6)
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
pp.pprint(tup)