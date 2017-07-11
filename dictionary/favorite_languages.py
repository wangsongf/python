favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

#字典中存储列表
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
for language in languages:
	print("\t" + language.title())