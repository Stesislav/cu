import random
print("Угадай число у тебя три попытки ")
a = random.randint(1,100)
chet = 0
while chet < 3:
    vvod = int(input("Введите число : "))
    if a > vvod:
        print("число меньше загаданного ")
        chet +=1
    elif a < vvod:
        print("число больше загаданного")
        chet +=1
    elif a == vvod:
        print("Победа")
        break
if chet == 3:
    print("вы проиграли")
    print(f"загаданное число:{ a }")
