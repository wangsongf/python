favorite_languages = {
<<<<<<< HEAD
=======
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

#字典中存储列表
favorite_languages = {
>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
<<<<<<< HEAD
	for language in languages:
		print("\t" + language.title())
=======
for language in languages:
	print("\t" + language.title())
>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7
