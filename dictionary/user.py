alien = {
	'color': 'red', 
	'point': '5', 
	'x_pos': '0', 
	'y_pos': '50'
	}
for key,value in alien.items():
	print("\nkey:"+key)
	print("\nvalue:"+value)


for name in alien.keys():
	print(name.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")