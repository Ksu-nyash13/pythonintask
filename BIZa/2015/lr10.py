# Задача 10. Вариант 18.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.
# Рыжова К.И.
# 12.10.16/08/12/16
print(
"""
		Добро пожаловать в раздел генератор персонажей!
		
		В ходе игры вам будут даны 4 характеристики: 
		   Сила, Ловкость, Здоровье и Мудрость.
	
		Также на старте у вас есть 30 пунктов, 
	которые вы можете распределить между этими характеристиками.
""")
Strength  = "Сила"
Health = "Здоровье"
Agility = "Ловкость"
Sapience = "Мудрость"
item = 30
while item > 0:
	characteristic = input("\nВыберите характестику: ")
	if characteristic == Strength:
		number1 = int(input("Введите значение, которое хотите присвоить характеристике Сила: "))
		print("Значение Силы - ", number1)
		item = item - number1
		print("У вас осталось",item,"единиц")
	elif characteristic == Health:
		number2 = int(input("Введите значение, которое вы хотите присвоить характеристике Здоровье: "))
		print("Значение Здоровья - ", number2)
		item = item - number2
		print("У вас осталось",item,"единиц")
	elif characteristic == Agility:
		number3 = int(input("Введите значение, которое вы хотите присвоить характеристике Ловкость: "))
		print("Значение Ловкости - ", number3)
		item = item - number3
		print("У вас осталось",item,"единиц")	
	elif characteristic == Sapience:
		number4 = int(input("Введите значение, которое вы хотите присвоить характеристике Мудрость: "))
		print("Значение Мудрости - ", number4)
		item = item - number4
		print("У вас осталось",item,"единиц")
	else:
		print("Такой характеристики нет.")
		
repeat = input("\nХотите что-нибудь изменить? (Да/Нет) ")
yes = "Да"
no = "Нет"
item = 0
while repeat == yes:
	characteristic = input("Выберите характестику для изменения: ")
	if characteristic == Strength:
		item = item + number1
		number11 = int(input("Введите значение, которое хотите присвоить характеристике Сила: "))
		print("Значение Силы - ", number11)
		item = item - number11
		print("У вас осталось",item,"единиц")	
		repeat = input("\nХотите что-нибудь изменить? (Да/Нет) ")
	elif characteristic == Health:
		item = item + number2
		number22 = int(input("Введите значение, которое вы хотите присвоить характеристике Здоровье: "))
		print("Значение Здоровья - ", number22)
		item = item - number22
		print("У вас осталось",item,"единиц")
		repeat = input("\nХотите что-нибудь изменить? (Да/Нет) ")
	elif characteristic == Agility:
		item = item + number3
		number33 = int(input("Введите значение, которое вы хотите присвоить характеристике Ловкость: "))
		print("Значение Ловкости - ", number33)
		item = item - number33
		print("У вас осталось",item,"единиц")
		repeat = input("\nХотите что-нибудь изменить? (Да/Нет) ")			
	elif characteristic == Sapience:
		item = item + number4
		number44 = int(input("Введите значение, которое вы хотите присвоить характеристике Мудрость: "))
		print("Значение Мудрости - ", number44)
		item = item - number44
		print("У вас осталось",item,"единиц")
		repeat = input("\nХотите что-нибудь изменить? (Да/Нет) ")

print("\nВы создали персонажа!")

		
input("Нажмите Enter, чтобы выйти")