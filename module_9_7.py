def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, res):
            if res % i == 0:
                print('Составное')
                flag = False
                break
            else:
                flag = True
        if flag == True:
            print('Простое')
        return res

    return wrapper


@is_prime
def sum_thtee(*args):
    # result = sum(args)
    result = 0
    for el in args:
        result += el
    return result


result1 = sum_thtee(2, 3, 6)
print(result1)

result2 = sum_thtee(2, 4, 6)
print(result2)
