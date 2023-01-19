
# ---------------------------------------------------------------------

# показывает среднее каждого значения из двух вводимых в процентах
# men = int (input ("Enter amount men: "))
# women = int (input ("Enter amount women: "))
# sum = men + women
# perc_men = (men /sum)*100
# perc_women = (women / sum)*100
# print (("%.f" %perc_men),("%.f" %perc_women))

# ---------------------------------------------------------------------
# программа спрашивает доход за неделю по дням и показывает сумму
# число_дней = 7
# total = 0.0
# for r in range (число_дней):
#     print("введите доход за ", r +1, "день",end="")
#     score=float(input(": "))
#     total+= score
# print (list,total)

# ---------------------------------------------------------------------

# калькулятор хотдогов для пикника с остатком
# кол_во_людей = int(input("enter amount people: "))
# кол_во_хотдогов = int(input("enter amount hotdogs : "))
# сосиски = 10
# булки = 8
# кол_во_людей = int(input('enter кол_во_людей: '))
# кол_во_хотдогов = int(input('enter кол_во_хотдогов: '))
# количество_сосисок = кол_во_людей * кол_во_хотдогов
# количество_булок = кол_во_людей * кол_во_хотдогов
# if кол_во_людей == 0 or кол_во_хотдогов == 0:
#     print('no party')
# else:
#     упаковок_сосисок = int(количество_сосисок // сосиски + 1)
#     print('упаковок_сосисок is: ', упаковок_сосисок)
#     оставшихся_сосисок = сосиски - количество_сосисок % сосиски
#     print('оставшихся_сосисок is: ', оставшихся_сосисок)
#     упаковок_булок = int(количество_булок / булки + 1)
#     print('количество_булок pack is: ', упаковок_булок)
#     осташихся_булок = булки - количество_булок % булки
#     print('осташихся_булок is: ', осташихся_булок)

# ---------------------------------------------------------------------
 
# калькулятор монет
# кол_во_монет_a= int(input('кол_во_монет 5-ти копе, чтобы их количество было равно рублю: '))
# кол_во_монет_b= int(input('кол_во_монет, 10-ти коп, чтобы их количество было равно рублю: '))
# кол_во_монет_c= int(input('кол_во_монет, 50-ти копб чтобы их количество было равно рублю: '))
# a=кол_во_монет_a*0.05
# b=кол_во_монет_b*0.10
# c=кол_во_монет_c*0.50
# if a+b+c == 1 or a+b==1 or a+c==1 or b+c==1:
#     print ("win")
# elif a+b+c>1 or a+b>1 or a+c>1 or b+c>1:
#     print ("amount more")
# elif a+b+c<1 or a+b<1 or a+c<1 or b+c<1:
#     print ("ampunt less")

# ---------------------------------------------------------------------
 
# датчик температуры с циклом повторения
# MAX_TEMP=102.5
# temperature = float(input("enter temperature: "))
# while temperature > MAX_TEMP:
#     print ("слишком высокая, убавьте нагрев")
#     temperature = float(input("enter temperature: "))
# print ("проверьте еще раз тут норм")

# ---------------------------------------------------------------------

# цикл с шагом 3 для 2 переменных 
# x = 10
# y = 30
# while x < y:
#     print(x, end=' ')
#     x = x + 3

# ---------------------------------------------------------------------

# цикл для слова с каждым разом меньше на 1 букву
# word = "pythonchik"
# while word:
#     print(word, end=" ")
#     # на каждой итерации убираем символ с конца
#     word = word[:-1]

# ---------------------------------------------------------------------

# цикл с накопительным эфектом
# total = 0
# for count in range (1,6):
#     total=total+count
#     print(total)

# ---------------------------------------------------------------------

# средний бал за введенное количество студентов ,оценок и введное количество лаб работ
# число_студентов = int(input("введите число студентов: "))
# число_оценок = int(input("введите число оценок: "))
# for student in range (число_студентов):
#     total = 0.0
#     print("номер студента", student + 1)
#     print("---------------------------")
#     for test_num in range (число_оценок):
#         print("номер лаб работы", test_num +1, end="")
#         score=float(input(": "))
#         total = total + score
#     average =  total / число_оценок
#     print ("Средний бал студента номер", student + 1, "составляет:", average)
#     print ()

# ---------------------------------------------------------------------

# цикл с повторить да - нет
# x = (input("повтроить цикл yes or not?: ")) 
# while x == "yes":
#     if x == "yes":
#         number_1 = int(input("enter number 1: "))
#         number_2 = int(input("enter number 2: "))
#         sum = number_1+number_2
#         print ("сумма чисел:", sum)
#     else: break
#     x = (input("повтроить цикл yes or not?: "))

# ---------------------------------------------------------------------

# диапазон от 0 до 1000 с шагом 10
# print(list(range(0, 1001, 10)))

# ---------------------------------------------------------------------

# повторяет введеное 10 раз
# x = (input("enter your name: "))
# for x in range(10):
#     print(x)

# ---------------------------------------------------------------------

# Эта программа вычисляет сумму серии чисел, вводимых пользователем (накопительный итог)
#  MAX = 5 # Максимальное число.
# Инициализировать накапливающую переменную.
# total = 0.0
# Объяснить, что мы делаем.
# print('Эта программа вычисляет сумму из')
# print(MAX, 'чисел, которые вы введете.')
# Получить числа и накопить их.
# for counter in range(MAX):
# number = int(input('Введите число: '))
# total = total + number
# Показать сумму чисел.
# print('Сумма составляет', total)
# Эта программа вычисляет сумму
# из 5 чисел, которые вы введете.
# Введите число: 1 Enter
# Введите число: 2 Enter
# Введите число: 3 Enter
# Введите число: 4 Enter
# Введите число: 5 Enter
# Сумма составляет 15.0

# ---------------------------------------------------------------------

# сумма чисел от 1 до 30
# n=1
# sum=0
# i=30
# while i <= n:
#     sum = sum+1
#     i=i+1
# print("Сумма чисел от 30 до 1:", sum)

# сумма чисел от 30 до 1
# number = int(input())
# summa = 0
# for i in reversed(range(number+1)):
#     # summa = summa + i
#     summa += i
# print(summa)

# ---------------------------------------------------------------------

# рисует кол-во строк и столбцов символами
# rows = int(input("Введи число: "))
# cols = int(input("Введи число: "))
# for r in range (rows):
#     for c in range (cols):
#         print ("-#-10", end="")
#     print()

# ---------------------------------------------------------------------

# цикл за какое время сколько проедешь с такой скоростью по часам
# v = int(input('Скорость: '))
# t = int(input('Время: '))
# for i in range(1, t+1):
#     print(i, v*i)

# ---------------------------------------------------------------------

# цикл for калькулятор цельсия фаренгейта
# end=20
# for number in range(1,end+1):
#     f=(9/5)*number+32
#     print(number, '\t', f)

# ---------------------------------------------------------------------

# геометрическая прогрессия
# # Запросим ввод параметров прогрессии с клавиатуры 
# n = int(input('Введите число элементов прогрессии: '))
# b_first = int(input('Введите первый элемент прогрессии: '))
# q = int(input('Введите знаменатель прогрессии: '))
# # Выведем первый элемент прогрессии
# print(b_first)
# # в переменной b_prev будем хранить значение предыдущего элемента
# # поместим в переменную b_prev значение первого элемента 
# b_prev = b_first
# # Для каждого элемента прогрессии, начиная с первого:
# for i in range(1,n):
#     # вычислим значение элемента,
#     b_cur = b_prev*q
#     # выведем его на экран,
#     print(b_cur)
#     # сохраним значение текущего элемента в переменной b_prev 
#     b_prev = b_cur

# ---------------------------------------------------------------------

# геометрическая прогрессия
# n = int(input('Введите количество дней: '))
# p=2
# b_first = 1
# q = 2
# b_prev = b_first
# for number in range(1,n+1):
#     for i in range(1,n):
#         b_cur = b_prev*q
#     print(number, '\t', b_cur)
#     b_prev = b_cur

# ---------------------------------------------------------------------

# задача про дни и зарплату (каждый день 1 копейка удваивается)
# y = int(input())
# k = 1
# print(1, k, sep = '\t')
# if y > 1:
#     for i in range(2, y+1):
#         k *= 2
#         print(i, k, sep = '\t')
# itog = (k*2) - 1
# print(k//100)

# ---------------------------------------------------------------------


# print ("введите положительные числа для их суммы \n или отрицательное для выхода: ")
# x = int(input("введите число: "))
# # # Запускаем цикл, пока пользователь не введет ноль 
# sum = 0
# kol = 0
# while x > 0:    
#     sum += x
#     x = int(input("Введите число: "))
# print ("Сумма чисел равна:",sum)

# ---------------------------------------------------------------------

# Плата за обучение повышает на 3% каждый год в течение следующих 5 лет.
# price = 45000
# year = 1
# while year < 6:
#     print(f'Год {year}, семестр 1, цена - {price}')
#     print(f'Год {year}, семестр 2, цена - {price}')
#     price *= 1.03
#     year += 1

#     price = 45000
# for year in range(1, 6):
#     print(f'Год {year}, семестр 1, цена - {price}')
#     print(f'Год {year}, семестр 2, цена - {price}')
#     price *= 1.03

# ---------------------------------------------------------------------

# Факториалы циклами
# n = int(input("введите не отрицательное число: "))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#     print(factorial)

# n = int(input("введите не отрицательное число: "))
# f=1
# for i in range(2,n+1):
#     f*=i
#     print(f)
#     n = int(input())

# ---------------------------------------------------------------------

# случайное число от 1 до 100 5 штук
# import random
# def main ():
#     for count in range (5):
#         number=random.randint (1,100)
#         print (number)
# main ()

# import random
# def main ():
#     number = random.randint (1,10)
#     print (number)
# main ()

# ---------------------------------------------------------------------

# располовинить число
# def main ():
#     value = float(int(input("Введите число, которое нужно располовинить: ")))
#     print ("Ваше число располовинили и оно будет равно: ",)
#     half (value)
    
# def half (number):
#     result = number/2
#     print( result)
# main ()

# ---------------------------------------------------------------------

# помесячное перечисление
# years = 1
# for currentYear in range(1, years + 1):
#       for currentMonth in range(1, 13):
#         monthly_rainfall = float(input("Enter the inches of rainfall for month " \
#             + format(currentMonth, "d") + ", year " \
#                 + format(currentYear,"d") + ": "))

# ---------------------------------------------------------------------

# Функция с результатом из другой функции
# def main():
#       value = int(input("введите стоимость: "))
#       print ("муни налог равен: ")
#       a = mun_tax(value)
#       print ("нал_на_иму равен:: ")
#       tax_tax(a)
# def mun_tax (value):
#       result = value*0.6
#       print (result)
#       return result
# def tax_tax(a):
#       result=(a/100)*72/100
#       print (result)
# main()

# ---------------------------------------------------------------------

# Сумма двух слуайных чисел с вопросом
# import random
# def main ():
      
     
#       print("первое число:")
#       a=number_1()
#       print("второе число:") 
#       b=number_2()
#       print(a, "\n" "+",b)
#       c = int(input("какой будет ответ"))
#       if a+b==c:
#             print("good")
#       else:
#             print ("not")
          
# def number_1():
#       for count in range (1):
#         number=random.randint (1,100)
#         print (number)
#         return number
# def number_2():
#       for count in range (1):
#         number=random.randint (1,100)
#         print (number)
#         return number
# main ()


# ---------------------------------------------------------------------

# записать в файл ранж цифр от 1 до 10
# def main():
#       outfile = open("numbers.txt", "w")
#       for i in range (1,11):
#             outfile.write(str(i)+ '\n')
#       outfile.close()
# main ()    

# ---------------------------------------------------------------------

# прочитать из файла все строки циклами while и for
# def main():
#       # Открыть файл numbers.txt для чтения.
#       sales_file=open('numbers.txt', 'r')
#       # Прочитать первую строку из файла, но пока не конвертировать в число.
#       # Сначала нужно вьполнить проверку на пустое строковое значение.
#       line = sales_file.readline()
#       # Продолжать обработку до тех пор, пока из readline
#       # не будет возвращена пустая строка.
#       while line != '':
#       # Конвертировать строку в число с плавающей точкой.
#             amount = float(line)
#       # Отформатировать и показать сумму
#             print(format(amount, '.2f'))
#       # Прочитать следующую строку
#             line = sales_file.readline()
#       # Закрыть файл.
#       sales_file.close()
# main ()

# def main():
#       # Открыть файл numbers.txt для чтения.
#       sales_file=open('numbers.txt', 'r')
#       # прочитать все строки из файла
#       for line in sales_file:
#             # конвертировать строку в число с плавающей точкой
#             amount = float(line)
#             # Отформатировать и показать сумму
#             print(format(amount, '.2f'))
#       # Закрыть файл.
#       sales_file.close()
# main ()

# ---------------------------------------------------------------------

# записывает текст в блокнот
# def main ():
#       outfile = open ("my_name.txt", "w")
#       outfile.write ("Ivan Ivanov")
#       outfile.close
# main()

# читает текст из файлы и выводит на экран
# def main ():
#       infile = open ("my_name.txt", "r")
#       file_contents = infile.read ()     
#       infile.close
#       print (file_contents)
# main()

# ---------------------------------------------------------------------

# записать в файл ранж цифр от 1 до 10
# def main():
#       outfile = open("numbers.txt", "w")
#       for i in range (1,11):
#             outfile.write(str(i)+ '\n')
#       outfile.close()
# main ()    

# читает текст из файлы и выводит на экран
# def main ():
#       infile = open ("numbers.txt", "r")
#       file_contents = infile.read ()     
#       infile.close
#       print (file_contents)
# main()

# сумма чисел из текста выше
# def main ():
      # открываем для чтения
#       infile = open ("numbers.txt", "r")
      # накопитель
#       total=0
      # переменная для подсчета
#       count=0
      # получаем значения из текст файла и склад их
#       for line in infile:
      # из строки в число с пл запятой
#             line = float(line)
#             count+=1
#             total+=line
#       infile.close
#       print (total)
# main()

# ---------------------------------------------------------------------

# записывает текст в блокнот
# def main ():
#       emp_file = open ("students.txt", "w")
#       name_student = "Джон Перц"
#       ocenka = "100"
#       emp_file.write(name_student+'\n')
#       emp_file.write(str(ocenka)+'\n')
#       emp_file.close
# main()

# удаляем опред строку из файла
# import os
# def main():
#       булевая в качестве флага
#       found = False
#       запрос на удаление
#       search = input("какое имя хотите удалить")
#       открываем исходник текст док
#       students_file = open ("students.txt", "r")
#       открываем временный
#       temp_file = open ("temp.txt", "w")
#       читаем поле с описанием первой записи
#       descr = students_file.readline()
#       читаем остаток файла
#       while descr != "":
#             читаем поле с количеством
#             qty=float(students_file.readline())
#             удаляем \n
#             descr=descr.rstrip('\n')
#             если эту запись не надо удалять пишем ее в временный тхт
#             if descr != search:
#                   пишем исходную запись в временный тхт
#                   temp_file.write(descr + '\n')
#                   temp_file.write(str(qty)+'\n')
#             else:
#                   назначаем флаг True
#                   found=True
#                   прочитываем след описание
#             descr = students_file.readline ()
#             закрываем тхт
#       students_file.close()
#       temp_file.close ()
#       один удаляем другой переимен вместо него
#       os.remove("students.txt")
#       os.rename('temp.txt', 'students.txt')
#       если нашел пишем 
#       if found:
#             print ("Файл обновлен")
#             не нашел что удалять пишем
#       else:
#             print ('не найдено')
# main ()

# ---------------------------------------------------------------------

# # записывает текст в блокнот
# def main ():
#       emp_file = open ("students.txt", "w")
#       name_student = "Джон Перц"
#       ocenka = "100"
#       emp_file.write(name_student+'\n')
#       emp_file.write(str(ocenka)+'\n')
#       emp_file.close
# main()

# # переименовываем опред строку из файла
# import os
# def main():
#       # булевая в качестве флага
#       found = False
#       # запрос на удаление
#       search = input("введите искомое")
#       new_qty = int(input("введите новое"))
#       # открываем исходник текст док
#       students_file = open ("students.txt", "r")
#       # открываем временный
#       temp_file = open ("temp.txt", "w")
#       # читаем поле с описанием первой записи
#       descr = students_file.readline()
#       # читаем остаток файла
#       while descr != "":
#             # читаем поле с количеством
#             qty=float(students_file.readline())
#             # удаляем \n
#             descr=descr.rstrip('\n')
#             # если эту запись не надо удалять пишем ее в временный тхт
#             if descr != search:
#                   запись новой во временный файл
#                   temp_file.write(descr + '\n')
#                   temp_file.write(str(new_qty)+'\n')
#                   # назначаем флаг True
#                   found=True                  
#             else:                  
#                   запись исх звпись во временный файл
#                   temp_file.write(descr + '\n')
#                   temp_file.write(str(qty)+'\n')
#                   # прочитываем след описание
#             descr = students_file.readline ()
#             # закрываем тхт
#       students_file.close()
#       temp_file.close ()
#       # один удаляем другой переимен вместо него
#       os.remove("students.txt")
#       os.rename('temp.txt', 'students.txt')
#       # если нашел пишем 
#       if found:
#             print ("Файл обновлен")
#             # не нашел что удалять пишем
#       else:
#             print ('не найдено')
# main ()

# ---------------------------------------------------------------------

# выводил на экран только первые 5 строк из файла
# with open("numbers.txt", 'r') as f:
#     for i in range(5):
#         print(f.readline())

# ---------------------------------------------------------------------

# запрос у пользователя ккой файл открыть и прказывает 5 строк из файла
# file_name=input("назовите файл который надо открыть")
# if input == file_name:
#     with open(file_name, 'r') as f:
#         for i in range(5):
#             print(f.readline())

# ---------------------------------------------------------------------

# нумерует строки в файле
# lines = 0
# file = open ("numbers.txt", 'r')
# for line in file:
#     lines +=1
#     print (lines,":", line)

# ---------------------------------------------------------------------

# читает текст из файла используя with
# with open ('names.txt') as s:
#     text = s.read()
#     print(text)

# читает текст из файла используя redline    
# file1 = open("names.txt", "r")
# while True:
#     # считываем строку
#     line = file1.readline()
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip())
# # закрываем файл
# file1.close

# читает текст из файла используя readlines
# # получим объект файла
# file1 = open("sample.txt", "r")
# # считываем все строки
# lines = file1.readlines()
# # итерация по строкам
# for line in lines:
#     print(line.strip())
# # закрываем файл
# file1.close

# ---------------------------------------------------------------------

# спрашивает кол-во случайных чисел, записывает их в файл, 
# считает их сумму и показывает на экране
# def main():
#     import random
#     outfile = open("random_numbers.txt", "w")
#     number = int(input("enter number for random: "))
#     for count in range (number):
#         number=random.randint (1,500)
#         outfile.write(str(number)+ '\n')
#     outfile.close()
#     with open ("random_numbers.txt") as s:
#         text = s.read()
#         print(text)
#     outfile = open ("random_numbers.txt", "r")
#     total=0
#     count=0
#     for line in outfile:
#         line = float(line)
#         count+=1
#         total+=line
#     outfile.close    
#     print ('сумма их будет равна: ',total)
# main()

# ---------------------------------------------------------------------

# делает список из вводимых пользователем в цифр
# a = list(map(int,input().split()))
# print (a)

# ---------------------------------------------------------------------

# делает список из вводимых пользователем в цифр выводит сумму,min,maxи среднюю
# print('Вводите значения цен, нажимайте enter')
# print(' для окончания ввода просто нажмите enter')

# a = int(input('-->> '))
# rices = []
# while True:
#     try:
#         rices.append(a)
#         a = int(input('-->> '))
#     except:
#         break
# b=sum(rices)
# c=min(rices)
# d=max(rices)
# e=b/len(rices)
# print(rices,b,c,d,e)

# ---------------------------------------------------------------------

# открывает файл и показывает в виде списка содержимое
# l = []
# with open('charge_accounts.txt') as f:
#     l = f.read().splitlines()
#     print (l)