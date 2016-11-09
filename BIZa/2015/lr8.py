import random
WORD = ("человек","животное","бактерия","паразит","рыба","птица","динозавр","насекомое","женщина","растение")
word = random.choice(WORD)
correct = word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
           Добро пожаловать в игру анаграммы!
        
   Надо переставить буквы так, чтобы получилось осмысленное слово
(Для выхода нажмите Enter, не вводя своей версии)
"""
)
print("\nВот анаграмма: ", jumble, "\nЕсли вам потребуется подсказка, напишите 'help'")
pomosch = "help"
point=2000
guess = input("\nВаш вариант: ")
while guess != correct and guess != "":	
	if guess == correct:
		print("Вы угадали!\n")
	elif guess == pomosch:
		print("Первая буква: ",correct[0])
		guess = input("Ваш вариант: ")
		point=point/2
	else:
		print("Неверный ответ")
		guess = input("Ваш вариант: ")
		
print("Спасибо за игру! Вы набрали", point, "очков")

input("\n\nНажмите Enter для выхода")
