class car_profile(object):
	def __init__(car):
		car.model=""
		car.name=""

	def getInfo(car):
		car.model=raw_input('Car model: ')
		car.name=raw_input('Car name: ')

	def printInfo(car):
		print car.model.upper() + ' ' + car.name.upper()

myCar=car_profile()
myCar.getInfo()
myCar.printInfo()