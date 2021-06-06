array = input(int("Введите произвольное количество целых чисел через пробел:"))
number = input(int("Введите целое число для поиска индекса числа (меньшего и большего или равного) в ведённой последовательности:"))

L = list(map(int, array.split())) #массив array (последовательность), преобразовываем в список

 def sort_array(L):
    for i in range(1, len(L)):
        x = L[i]
        idx = i
        while idx > 0 and L[idx - 1] > x:
            L[idx] = L[idx - 1]
            idx -= 1
        L[idx] = x

 def binary_search(L, number, left, right)
    middle = (right + left) // 2
    if number < L[0]:
        print("Нет числа меньше введёного")
    elif L[middle] == number:
        a = L[:middle]
        for i in a:
            if i == number:
                a.remove(i)
        idx_1 = (len(a) - 1)
        if idx_1 < 0:
            print ("Нет числа меньше заданного")
        else:
            b = L[middle:]
            for j in b:
                if j < number and len(b) > 1:
                    b.remove(j)
            ind = b[0]
            idx_2 = L.index(ind)
            if idx_2 == len(L) - 1:
                print("В списке нет числа больше числа с индексом", idx_2)
            else:
                print(idx_1, idx_2)
                return idx_1, idx_2
    elif number < L[middle]:
        return binary_search(L, number, left, middle - 1)
    else:
        return binary_search(L, number, middle + 1, right)
