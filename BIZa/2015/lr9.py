import random
print("Компьютер загадывает вам женский аксессуар, вы должны его угадать")
Words=("серьги", "колье", "кольцо", "заколка", "палантин", "шляпа", "перчаткм", "сумка", "брошь", "браслет")
word=random.choice(Words)
print("Первая буква: ", word[0])
print("Длина слова: ", len(word))
print("Вы можете отгадать буквы. У вас есть 5 попыток.")
circle=1

while circle < 6:
 letter = input("")
 res = word.find(letter)
 if res >= 1:
     print("Да")
 else:
     print("Нет")
 circle+=1
Name = input("Введите слово: ")
if Name==word:
  print("Вы угадали!")
else:
   print("Вы проиграли.")
input("Нажмите Enter для выхода")
	
   
