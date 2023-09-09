# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def In_Range(list_in, range_min, range_max):
    list_res = []
    
    for i in range(len(list_in)):
        if range_min <= list_in[i] <= range_max:
            list_res.append(i)
        
    return list_res    


list_in = [1, 5, 88, 100, 2, -4]
range_min = 33
range_max = 200


print(In_Range(list_in, range_min, range_max))
