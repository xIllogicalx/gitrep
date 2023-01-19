# # Запрашиваем ввод у пользователя
# x = int(input("Введите целое число (0 для выхода): ")) 
# # Запускаем цикл, пока пользователь не введет ноль 
# while x != 0:
#     # Положительное или отрицательное? 
#     if x > 0:
#         print("Это положительное число.") 
#     else:
#         print("Это отрицательное число.")
# # Запрашиваем очередное значение
#     x = int(input("Введите целое число (0 для выхода): "))

# # Запрашиваем у пользователя верхнюю границу
# limit = int(input("Введите целое число: "))
# # Выводим все числа, кратные трем, вплоть до указанного пользователем значения
# print("Все числа, кратные трем, вплоть до", limit, ":") 
# for i in range(3, limit + 1, 3):
#     print(i)

# # Запрашиваем у пользователя сообщение
# message = input("Введите сообщение (оставьте его пустым для выхода): ") 
# # Начало цикла, пока сообщение не станет пустым
# while message != "":
#     # Запрашиваем количество повторений
#     n = int(input("Сколько раз повторить сообщение? ")) 
# # Показываем сообщение заданное количество раз
#     for i in range(n):
#         print(message)
# # Запрашиваем следующее сообщение
#     message = input("Введите сообщение (оставьте его пустым для выхода): ")

# sum(list)/len(list) - среднее из списка


# # Запрашиваем ввод у пользователя
# x = input("Введите список чисел, разделенных пробелом: ").split()
# num_list = list(map(int, x))
# # Запускаем цикл, пока пользователь не введет ноль 
# while x != 0:    
#     print ("средняя списка:", sum(num_list)/len(num_list))
#     x = int(input("Введите целое число (0 для выхода): "))

# (32 °C × 9/5) + 32 = 89,6 °F

# i = 101
# print("градусы цельсия кратные 10 от нуля до ста", " - ", i)
# # for x in range(0,101,10):
# #     print("градусы фаренгейта кратные 10 от нуля до ста", " - ", x)

# for y in range(0,(i*9)//5+32,10):
#     print("фаренгейт",y)


# num = float(input("Введите число: "))
# x1 = -1 * num
# x2 = x1 // 1
# x3 = x2*-1
# x4 = float(x3)
# print("налик: ", round(x4,2))





# х = int(input("ведите число: "))
# x1 = (x+2)
# # print ("ваша сумма: ",(-1 * x // 1 * -1))
# # (-1*x//1*(-1))
# # print("ваша сумма: ", x)

# PENNIES_PER_NICKEL = 5
# NICKEL = 0.05
# # Собираем общую сумму
# total = 0.00
# # Запрашиваем цену первого товара как строку
# line = input("Введите цену товара (пустая строка для выхода): ")
# # Продолжаем запрашивать цены товаров, пока строка не будет оставлена пустой
# while line != "":
#  # Добавляем цену в общей сумме (после перевода ее в число с плавающей запятой)
#     total = total + float(line)
#  # Запрашиваем цену следующего товара
#     line = input("Введите цену товара (пустая строка для выхода): ")
# # Показываем полную сумму к оплате
# print("Полная сумма к оплате: %.02f" % total)
# # Считаем, сколько центов осталось бы, если бы мы оплатили всю покупку 5–центовыми монетами
# rounding_indicator = total * 100 % PENNIES_PER_NICKEL
# if rounding_indicator < PENNIES_PER_NICKEL / 2:
# # Если оставшаяся сумма центов меньше 2,5, округляем значение путем вычитания
# # полученного количества центов из общей суммы
#     cash_total = total - rounding_indicator / 100
# else:
# # Иначе добавляем 5 центов и затем вычитаем нужное количество центов
#     cash_total = total + NICKEL - rounding_indicator / 100
# # Выводим итоговую сумму для оплаты
# print("Сумма для оплаты наличными: %.02f" % cash_total)

##
# # Рассчитаем периметр многоугольника, построенного на основании координат точек,
# # введенных пользователем. Пустая строка завершает ввод данных
# from math import sqrt
# # Переменная для хранения периметра многоугольника
# perimeter = 0
# # Запрашиваем координаты первой точки
# first_x = float(input("Введите первую координату X: "))
# first_y = float(input("Введите первую координату Y: "))
# # Инициализируем координаты предыдущей точки начальными значениями
# prev_x = first_x
# prev_y = first_y
# # Запрашиваем остальные координаты
# line = input("Введите следующую координату X (Enter для окончания ввода): ")
# while line != "":
#     # Преобразуем координату X в число и запрашиваем координату Y
#     x = float(line)
#     y = float(input("Введите следующую координату Y: "))
#     # Рассчитываем расстояние до предыдущей точки и добавляем к периметру
#     dist = sqrt((prev_x - x) ** 2) + ((prev_y - y) ** 2)
#     perimeter = perimeter + dist
#     # Устанавливаем значения предыдущих координат
#     # для следующей итерации
#     prev_x = x
#     prev_y = y
#     # Запрашиваем следующую координату X
#     line = input("Введите следующую координату X (Enter для окончания ввода): ")
# # Рассчитываем расстояние от последней точки до первой и добавляем к периметру
# dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)

# perimeter = perimeter + dist
# # Отображаем результат
# print("Периметр многоугольника равен", perimeter)


# A = 4.0
# A_MINUS = 3.7
# B_PLUS = 3.3
# B = 3.0
# B_MINUS = 2.7
# C_PLUS = 2.3
# C = 2.0
# C_MINUS = 1.7
# D_PLUS = 1.3
# D = 1.0
# F = 0
# INVALID = -1

# letter = input("Введите буквенную оценку): ")
# letter = letter.upper()
# if letter == "A+" or letter == "A":
#     gp = A
# elif letter == "A-":
#     gp = A_MINUS
# elif letter == "B+":
#     gp = B_PLUS
# elif letter == "B":
#     gp = B
# elif letter == "B–":
#     gp = B_MINUS
# elif letter == "C+":
#     gp = C_PLUS
# elif letter == "C":
#     gp = C
# elif letter == "C–":
#     gp = C_MINUS
# elif letter == "D+":
#     gp = D_PLUS
# elif letter == "D":
#     gp = D
# elif letter == "F":
#     gp = F
# else:
#     gp = INVALID

# if gp == INVALID:
#     print("Введена некорректная оценка.")
# else:
#      print("Буквенная оценка", letter, "соответствует", gp, "баллам.")

##
# Рассчитать стоимость посещения зоопарка для группы
#
# Константы для хранения цен на разные категории билетов
# BABY_PRICE = 0.00
# CHILD_PRICE = 14.00
# ADULT_PRICE = 23.00
# SENIOR_PRICE = 18.00
# # Сохраним как константы возрастные ограничения
# BABY_LIMIT = 2
# CHILD_LIMIT = 12
# ADULT_LIMIT = 64
# # Переменная для хранения общей суммы посещения
# total = 0
# # Читаем ввод пользователя до пустой строки
# line = int(input("Введите возраст посетителя (пустая строка для окончания ввода): "))
# while line != "":
#     age = int(line)
#  # Добавляем цену билета к общей сумме
#     if age <= BABY_LIMIT:
#         total = total + BABY_PRICE
#     elif age <= CHILD_LIMIT:
#         total = total + CHILD_PRICE
#     elif age <= ADULT_LIMIT:
#         total = total + ADULT_PRICE
#     else:
#         total = total + SENIOR_PRICE
#  # Считываем возраст следующего посетителя
#     line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# # Отображаем сумму группового посещения с правильным форматированием
# print("Сумма посещения зоопарка для этой группы составит $%.2f" % total)

# # число:
# n = 0
# # сумма:
# sum_n = 0
# # количество:
# count = 0
# while True:
#     a = int(input())
 
#     # Если 0:
#     if a == 0:
#         break
#     else:
#         sum_n += a
#         count += 1
# print('сумма: ', sum_n)
# print('количество: ', count)
# print('среднее значение:', sum_n / count)

##
# Определение оценки работы сотрудников при помощи рейтингов от пользователя
# #
# RAISE_FACTOR = 2400.00
# UNACCEPTABLE = 0
# ACCEPTABLE = 0.4
# MERITORIOUS = 0.6
# # Запрашиваем у пользователя рейтинг
# rating = float(input("Введите рейтинг: "))
# # Классифицируем сотрудников
# if rating == UNACCEPTABLE:
#     performance = "низкий"
# elif rating == ACCEPTABLE:
#     performance = "удовлетворительный"
# elif rating >= MERITORIOUS:
#     performance = "высокий"
# else:
#     performance = ""
#     #Выводим результат
# if performance == "":
#     print("Введен ошибочный рейтинг.")
# else:
#       print("Основываясь на введенном рейтинге, ваш уровень: %s." % performance)
# print("Прибавка к зарплате составит: $%.2f." % (rating * RAISE_FACTOR))
 



# minutes = int(input("Введите число минут в месяц: "))
# sms = int(input("Введите число смс в месяц: "))
# payment = 15
# tax = 0.44

# if minutes < 50 and sms < 50:
#     standart_price=payment+((payment+tax)*0.05)
#     print("налог на 911: ", tax, "$")
#     print("Сумма налога","%2f"%((payment+tax)*0.05),"$")
#     print("вы должны зхаплатить","%2f"%standart_price,"$")
# elif minutes>50:
#     add_mins=0.25
#     add_sms=0.15
#     min_not_in_tarif=minutes-50
#     sms_not_in_tarif=sms-50
#     add_min_price=((min_not_in_tarif)*add_mins)
#     add_sms_price=((sms_not_in_tarif)*add_sms)
#     full_price=payment+add_sms_price+add_min_price+((payment+add_sms_price+add_min_price)*0.05)
#     print('Ваш базовый тариф за 50 минут и 50 смс составит',payment, "$")
#     print("налог на 911: ", tax, "$")
#     print("Общая сумма состаит","%.2f"%((payment+add_sms_price+add_min_price)*0.05),"$")
#     print('Вы тратите дополнительные',min_not_in_tarif,'минут,и дополнительно',sms_not_in_tarif,'смс')
#     print('общая цена будет','%.2f'%full_price,'USD')
# elif sms>50:
#     add_mins=0.25
#     add_sms=0.15
#     min_not_in_tarif=minutes-50
#     sms_not_in_tarif=sms-50
#     add_min_price=((min_not_in_tarif)*add_mins)
#     add_sms_price=((sms_not_in_tarif)*add_sms)
#     full_price=payment+add_sms_price+add_min_price+((payment+add_sms_price+add_min_price)*0.05)
#     print('Ваш базовый тариф за 50 минут и 50 смс составит',payment, "$")
#     print("налог на 911: ", tax, "$")
#     print("Общая сумма состаит","%.2f"%((payment+add_sms_price+add_min_price)*0.05),"$")
#     print('Вы тратите дополнительные',min_not_in_tarif,'минут,и дополнительно',sms_not_in_tarif,'смс')
#     print('общая цена будет','%.2f'%full_price,'USD')

##
# Определяем, високосный заданный год или нет
#
# Запрашиваем у пользователя год
# year = int(input("Введите год: "))
# # Определяем, високосный или нет
# if year % 400 == 0:
#     isLeapYear = True
# elif year % 100 == 0:
#     isLeapYear = False
# elif year % 4 == 0:
#     isLeapYear = True
# else:
#     isLeapYear = False
# # Отображаем результат
# if isLeapYear:
#     print(year, " – високосный год.")
# else:
#     print(year, " – невисокосный год.")


# year = int(input("Input a year: "))
# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False
# month = int(input("Input a month [1-12]: "))
# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30
# day = int(input("Input a day [1-31]: "))
# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))



## Определяем формат номерного знака. Всего допустимых формата два:
# 1) 3 буквы и 3 цифры
# 2) 4 цифры 3 буквы
# # Запрашиваем номер у пользователя
# plate = input("Введите номерной знак машины: ")
# # Проверяем номерной знак. Необходимо проверить все 6 знаков для номера старого образца
# # и 7 знаков – для нового
# if len(plate) == 6 and \
# plate[0] >= "A" and plate[0] <= "Z" and \
# plate[1] >= "A" and plate[1] <= "Z" and \
# plate[2] >= "A" and plate[2] <= "Z" and \
# plate[3] >= "0" and plate[3] <= "9" and \
# plate[4] >= "0" and plate[4] <= "9" and \
# plate[5] >= "0" and plate[5] <= "9":
#     print("Это номерной знак старого образца.")
# elif len(plate) == 7 and \
# plate[0] >= "0" and plate[0] <= "9" and \
# plate[1] >= "0" and plate[1] <= "9" and \
# plate[2] >= "0" and plate[2] <= "9" and \
# plate[3] >= "0" and plate[3] <= "9" and \
# plate[4] >= "A" and plate[4] <= "Z" and \
# plate[5] >= "A" and plate[5] <= "Z" and \
# plate[6] >= "A" and plate[6] <= "Z":
#     print("Это номерной знак нового образца.")
# else:
#     print("Неверный номерной знак.")

#
# for i in range(1, 101):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3==0:
#             print('Fizz')
#     elif i%5==0:
#             print('Buzz')
#     else:
#         print(i)



# def drawBox(): 
#     print("**********") 
#     print("*        *") 
#     print("*        *") 
#     print("**********")




# ## Рисуем прямоугольник из звездочек, заполненный пробелами 
# # @param width – ширина прямоугольника
# # @param height – высота прямоугольника
# def drawBox(width, height):
# # Слишком маленькие прямоугольники не могут быть нарисованы 
# # при помощи этой функции 
#     if width < 2 or height < 2:
#         print("Ошибка: ширина или высота прямоугольника слишком малы.") 
#         quit()
# # Рисуем верхнюю линию прямоугольника 
#     print("*" * width)
# # Рисуем стороны прямоугольника 
#     for i in range(height - 2):
#         print("*" + " " * (width - 2) + "*")
#     print("*" * width)
# drawBox(15, 10)

## Рисуем прямоугольник
# @param width – ширина прямоугольника
# @param height – высота прямоугольника
# @param outline – символ для рисования сторон прямоугольника 
# # @param fill – символ для заливки прямоугольника
# def drawBox(width, height, outline, fill):
# # Слишком маленькие прямоугольники не могут быть нарисованы при помощи этой функции 
#     if width < 2 or height < 2:
#         print("Ошибка: ширина или высота прямоугольника слишком малы.") 
#         quit()
# # Рисуем верхнюю линию прямоугольника 
#     print(outline * width)
# # Рисуем стороны прямоугольника 
#     for i in range(height-2):
#         print(outline + fill*(width-2)+outline)
# # Рисуем нижнюю линию прямоугольника 
#     print(outline * width)
# # Демонстрируем работу обновленной функции 
# drawBox(14, 5, "@", ".")

# def drawBox(width, height, outline="*", fill=" "):
#     drawBox(14, 5, "@", ".")

## Вычислить сумму первых n элементов геометрической прогрессии
# @param a – первый элемент последовательности
# @param r – знаменатель последовательности
# @param n – количество элементов, сумму которых необходимо получить 
# @return s – сумма первых n элементов
def sumGeometric(a, r, n):
 # Вычисляем и возвращаем сумму первых n элементов при r, равном 1 
    if r == 1:
        return a * n
# Вычисляем и возвращаем сумму первых n элементов при r, не равном 1 
    s=a*(1-r**n)/(1-r)
    return s




def main():
    # Запрашиваем значение переменной a для первой последовательности 
    init = float(input("Введите значение переменной a (0 для выхода): "))
# Пока вводимое значение не равно нулю 
    while init != 0:
# Запрашиваем знаменатель и количество элементов
        ratio = float(input("Введите знаменатель последовательности, r: ")) 
        num = int(input("Введите количество элементов, n: "))
# Вычисляем и отображаем результат
        total = sumGeometric(init, ratio, num)
        print("Сумма первых", num, "элементов равна", total)
# Запрашиваем значение переменной a для следующей последовательности 
        init = float(input("Введите значение переменной a (0 для выхода): "))
# Вызываем основную функцию 
main()

