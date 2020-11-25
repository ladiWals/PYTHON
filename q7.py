def binary(number):
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    if number == 0:
        return '0'
    return result
