def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__ : func(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# #функция принимает список чисел и набор функций.
# потом идет цикл: в переменную func записывается функция (напр max)
# и в словарь добавляется пара: ключ - имя функции, значение - результат этой функции.
# и так пока не береберет все функции.