from random import randint

def gen_random(count, begin, end):
    try:
        assert count > 0
    except:
        print("Вы не указали кол-во чисел")
        pass

    result_list = [randint(begin, end) for index in range(count)]
    return result_list

def main():
    print(str(gen_random(5, 1, 3))[1:-1])
    print(str(gen_random(2, 0, 10))[1:-1])
    print(str(gen_random(10, 0, 99))[1:-1])

if __name__ == "__main__":
    main()
