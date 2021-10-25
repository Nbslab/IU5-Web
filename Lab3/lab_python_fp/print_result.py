def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        return_value = func(*args)
        if type(return_value) == list:
            for value in return_value:
                print (value)
        elif type(return_value) == dict:
            for key, value in return_value.items():
                print(f'{key} = {value}')
        else:
            print(return_value)
        return return_value
    return decorated_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
