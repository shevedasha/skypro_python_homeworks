class User: #класс

	def __init__(self, first_name, last_name): #конструктор
		self.first_name = first_name #поле класса
		self.last_name = last_name
		
	def sayFirst(self): #метод
		print("Имя", self.first_name)	
	def sayLast(self):
		print("Фамилия", self.last_name)
	def sayFull(self):
	    print("Имя и фамилия", f'{self.first_name} {self.last_name}')
	