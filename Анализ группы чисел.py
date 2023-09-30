import math

def sort_asc(group):
    return sorted(group)

def sort_desc(group):
    return sorted(group, reverse=True)

def sum_of_numbers(group):
    return sum(group)

def average(group):
    return sum(group) / len(group)

def median(group):
    sorted_group = sorted(group)
    length = len(sorted_group)
    if length % 2 == 0:
        return (sorted_group[length // 2 - 1] + sorted_group[length // 2]) / 2
    else:
        return sorted_group[length // 2]

def mode(group):
    counts = {}
    for number in group:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    modes = [number for number, count in counts.items() if count == max_count]
    return modes[0], max_count

def minimum(group):
    return min(group)

def maximum(group):
    return max(group)

def count_even(group):
    return sum(1 for number in group if number % 2 == 0)

def count_odd(group):
    return sum(1 for number in group if number % 2 != 0)

def sum_even(group):
    return sum(number for number in group if number % 2 == 0)

def sum_odd(group):
    return sum(number for number in group if number % 2 != 0)

def count_positive(group):
    return sum(1 for number in group if number > 0)

def count_negative(group):
    return sum(1 for number in group if number < 0)

def difference_max_min(group):
    return max(group) - min(group)

def most_common(group):
    counts = {}
    for number in group:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    modes = [number for number, count in counts.items() if count == max_count]
    return modes[0], max_count

def arithmetic_mean(group):
    return sum(group) / len(group)

def max_number(group):
    return max(group)

def min_number(group):
    return min(group)

def square_root_elements(group):
    return [math.sqrt(number) if number >= 0 else None for number in group]

def sum_of_two_largest(group):
    sorted_group = sorted(group)
    return sorted_group[-1] + sorted_group[-2]

def sum_of_two_smallest(group):
    sorted_group = sorted(group)
    return sorted_group[0] + sorted_group[1]

def length_of_group(group):
    return len(group)

def product_of_numbers(group):
    result = 1
    for number in group:
        result *= number
    return result

def divisibility(group):
    count = 0
    for number in group:
        if number % len(group) == 0:
            count += 1
    return count


user_input = input("Введите числа через пробел: ")
group = [float(number) for number in user_input.split()]
print("Длина списка чисел:", length_of_group(group))
print("Отсортированная группа чисел в порядке возрастания:", sort_asc(group))
print("Отсортированная группа чисел в порядке убывания:", sort_desc(group))
print("Сумма всех чисел в группе:", sum_of_numbers(group))
print("Среднее значение чисел в группе:", average(group))
print("Медиана группы чисел:", median(group))
print("Мода группы чисел:", mode(group))
print("Наименьшее число в группе:", minimum(group))
print("Наибольшее число в группе:", maximum(group))
print("Количество чётных чисел в группе:", count_even(group))
print("Количество нечётных чисел в группе:", count_odd(group))
print("Сумма чётных чисел в группе:", sum_even(group))
print("Сумма нечётных чисел в группе:", sum_odd(group))
print("Количество положительных чисел:", count_positive(group))
print("Количество отрицательных чисел:", count_negative(group))
print("Разность между наибольшим и наименьшим числом:", difference_max_min(group))
print("Самое частое число в списке(количество повторений):", most_common(group))
print("Среднее арифметическое:", arithmetic_mean(group))
print("Максимальное число в группе:", max_number(group))
print("Минимальное число в группе:", min_number(group))
print("Квадратные корни из чисел в группе:", square_root_elements(group))
