<<<<<<< HEAD
#返回字典
def build_person(first_name, last_name):
	"""返回一个字典， 其中包含有关一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_new_person(first_name, last_name, age=''):
	"""返回一个字典， 其中包含有关一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_new_person('jimi', 'hendrix', age=27)
print(musician)
=======

def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7