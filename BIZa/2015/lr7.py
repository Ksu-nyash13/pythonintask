import random
wifes=("Метида", "Фемида", "Гера")
wife = random.choice(wifes)
print("Угадайте имя одной из трех официальныхж жен Зевса")
name = input("")
point = 2000
while name != wife:
 if name == wife:
     print(point)	
 else:
     print("Вы не угадали!")
     name = input("Попробуйте еще раз ")
     point = point/2   
print("Поздравляем, вы угадали. Вы получаете", point, "очков")
input("Нажмите Enter для выхода")