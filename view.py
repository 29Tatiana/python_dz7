import logger
import validator

num1 = ''
num2 = ''
sign = ''
mode = ''

def get_complex_num():
    num = ''
    while not validator.validate_num('\(?\-?\d+(?:\.\d+)?\s?[+-]\s?\d+(?:\.\d+)?j\)?', num):
        num = input('Введите комплексное число в формате a + bj: ')
        if not validator.validate_num('\(?\-?\d+(?:\.\d+)?\s?[+-]\s?\d+(?:\.\d+)?j\)?', num):
            print('Введено неверное число. Попробуйте снова.')
    return num

def get_rational_num():
    num = ''
    while not validator.validate_num('\-?[1-9]\d*(?:\/[1-9]\d*)?', num):
        num = input('Введите рациональное число в формате a/b: ')
        if not validator.validate_num('\-?[1-9]\d*(?:\/[1-9]\d*)?', num):
            print('Введено неверное число. Попробуйте снова.')
    return num
def get_sign():
    sign = ''
    while not validator.validate_num('[\+\-\*\/]', sign):
        sign = input('Введите операцию (+, -, *, /): ')
        if not validator.validate_num('[\+\-\*\/]', sign):
            print('Неверный арифметический оператор. Попробуйте снова.')
    return sign

def get_mode():
    global mode
    print('С какими числами вы планируете работать?')
    mode = input('Рациональные - 0\nКомплексные - 1\nВведите 0 или 1: ')
    if mode == '0' or mode == '1':
        return int(mode)
    else:
        print('Ошибка! Введите 0 или 1.')

def get_data():
    global num1
    global sign
    global num2
    global mode
    if mode == '0':
        num1 = get_rational_num()
    else:
        num1 = get_complex_num()
    sign = get_sign()
    if mode == '0':
        num2 = get_rational_num() 
    else:
        num2 = get_complex_num()
    return num1, sign, num2

def view_data(result):
    res_str = f'{num1} {sign} {num2} = {result}'
    logger.add_to_log(res_str)
    print(res_str)        