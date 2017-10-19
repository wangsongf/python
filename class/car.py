class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
<<<<<<< HEAD
	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值
		拒绝将里程表往回拨
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
=======
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

>>>>>>> 8f686a6b5c580976db52dab0e8b922a1878856e7
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()