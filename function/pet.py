<<<<<<< HEAD
#位置实参
=======

>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
<<<<<<< HEAD

#关键字实参
def describe_pet(animal_type, pet_name):
"""显示宠物的信息"""
print("\nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

#默认值
def describe_pet(pet_name, animal_type='dog'):
"""显示宠物的信息"""
print("\nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

#等效函数调用
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
=======
>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7