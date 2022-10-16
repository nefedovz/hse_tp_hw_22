def _min(array):
    min_num = array[0]
    for i in range(1, len(array)):
        if min_num > array[i]:
            min_num = array[i]
    return min_num


def _max(array):
    max_num = array[0]
    for i in range(1, len(array)):
        if max_num < array[i]:
            max_num = array[i]
    return max_num

def _sum(array):
    sum_def = array[0]
    for i in range(1, len(array)):
        sum_def += array[i]
    return sum_def

def _mult(array):
    mult_def = array[0]
    for i in range(1, len(array)):
        mult_def *= array[i]
    return mult_def

if __name__ == "__main__":
    data = open(input("Введите название файла: ")).readline()
    array = [int(x) for x in data.split()]
    action = 6
    while True:
        if action == 1:
            print("Минимальное число:", _min(array))
            action = 6
            continue
        elif action == 2:
            print("Максимальное число:", _max(array))
            action = 6
            continue
        elif action == 3:
            print("Сумма всех чисел:", _sum(array))
            action = 6
            continue
        elif action == 4:
            print("Произведение всех чисел:", _mult(array))
            action = 6
            continue
        elif action == 5:
            break
        else:
            print("Выберите действие:", "1. Найти минимальное число;", "2. Найти максимальное число;", "3. Найти сумму всех чисел;", "4. Найти произведение всех чисел;", '5. Завершить работу программы.', sep='\n')
            action = int(input())