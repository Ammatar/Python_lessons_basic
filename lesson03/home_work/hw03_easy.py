# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number_temp1 = number*(10**ndigits)
    number_temp_ostatok = number_temp1 % 1
    #print(number_temp_ostatok)
    if number_temp_ostatok > 0.4:
        number_add = 1 - number_temp_ostatok
        round_number = number + (number_add/(10**ndigits))
    else:
        number_add = number_temp_ostatok - 1
        round_number = number - (number_add/(10**ndigits))
    #print(round_number)
    return round_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_map = list(map(int, str(ticket_number)))
    try:
        ticket_part_1 = ticket_number_map[0] + ticket_number_map[1] + ticket_number_map[2]
    except IndexError:
        pass
    try:
        ticket_part_2 = ticket_number_map[3]+ ticket_number_map[4]+ticket_number_map[5]
    except IndexError:
        pass
    try:
        result = ticket_part_1 == ticket_part_2
        return (result)
    except:
        pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
