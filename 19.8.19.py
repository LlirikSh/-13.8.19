bil = int(input("Введите количество билетов, которые хотите приобрести:"))
suma = 0
for i in range(bil):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        suma = suma + 0
    elif 18 <= age < 25:
        suma = suma + 990
    else:
        suma = suma + 1390
if bil > 3:
    suma = suma-((suma*10)/100)
    print("Ваша скидка составила 10%")
print("С вас:" + " " + str(int(suma)) + " " + "рублей")
print("Хорошего отдыха")
