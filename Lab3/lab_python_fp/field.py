goods = [
    {'title': 'Ковер', 'price': 2000, 'colour': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'colour': 'black'}
]


def field(items, *args):
    try:
        assert len(items) != 0 and len(args) != 0
    except:
        print("Вы не передали аргументы")
    return_list = []
    for item in items:
        temp_dict = {}
        if len(args) == 1:
            for key, value in item.items():
                if key in args and value != None:
                    return_list.append(value)
        else:
            for key, value in item.items():
                if key in args and value != None:
                    temp_dict[key] = value
            if len(temp_dict) > 0:
                return_list.append(temp_dict)

    return return_list


def main():
    print(str(field(goods, 'title'))[1:-1])
    print(str(field(goods, 'title', 'price'))[1:-1])
    print(str(field(goods, 'title', 'price', 'colour'))[1:-1])


if __name__ == "__main__":
    main()
