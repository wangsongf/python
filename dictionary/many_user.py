<<<<<<< HEAD
#在字典中去嵌套字典
=======
#在字典中存储字典
>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

name = input("Please enter your name: ")
print("Hello, " + name + "!")