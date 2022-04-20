def optimal_predict(number: int = 1) -> int:
    '''Игра компьютер угадает число меньше чем за 20 попыток'''

    import numpy as np

    min = 1
    max = 101

    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
        mid = (min+max) // 2
    
        if mid > number:
          max = mid
    
        elif mid < number:
          min = mid

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return count