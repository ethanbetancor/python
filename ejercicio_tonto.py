import random
puntuacion = 0
for cont in range(1,11):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(num1, "x", num2)
    guess = int(input("resultado ="))
    if num1 * num2 == guess:
        puntuacion += 10
        print("Correcto Aitana, eres la mejor!")
    else:
        print("terrible")
print("tu puntuacion final es", puntuacion)
