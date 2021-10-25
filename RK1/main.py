from operator import itemgetter


# Создаем класс-таблицу Компьютер
class PC:
    def __init__(self, id, name, os):
        self.id = id
        self.name = name
        self.os = os


# Создаем класс-таблицу Программа
class Prog:
    def __init__(self, id, name, id_pc, storage_usage):
        self.id = id
        self.name = name
        self.storage_usage = storage_usage
        self.id_pc = id_pc


# Создаем класс-таблицу Программа-Компьютер для реализации связи М-М
class ProgPC:
    def __init__(self, id_pc, id_prog):
        self.id_pc = id_pc
        self.id_prog = id_prog


# Заполняем класс-таблицу Программа тестовыми данными
programs = [
    Prog(1, 'VSCode', 3, 1.5),
    Prog(2, 'PYCharm', 1, 2),
    Prog(3, 'Google Chrome', 4, 3),
    Prog(4, 'VM VirtualBox', 2, 10),
    Prog(5, 'Slack', 5, 4),
    Prog(6, 'Spotify', 3, 3.3),
    Prog(7, 'Zoom', 1, 2.4),
    Prog(8, 'Telegram', 3, 2.4),
    Prog(9, 'Discord', 2, 4),
]

# Заполняем класс-таблицу Компьютер тестовыми данными
comps = [
    PC(1, 'Asus', 'Windows'),
    PC(2, 'Acer', 'Windows'),
    PC(3, 'MacBook', 'MacOS'),
    PC(4, 'Lenovo', 'Windows'),
    PC(5, 'PC551', 'Linux'),
]

# Заполняем класс-таблицу Программа-Компьютер тестовыми данными
prog_pc = [
    ProgPC(1, 2),
    ProgPC(1, 7),
    ProgPC(2, 4),
    ProgPC(2, 9),
    ProgPC(3, 1),
    ProgPC(3, 6),
    ProgPC(3, 8),
    ProgPC(4, 3),
    ProgPC(5, 5),
]


def main():
    print('Задание E1')
    # Соединение данных один-ко-многим
    one_to_many = [(pr.name, pr.storage_usage, pc.name, pc.os)
                   for pc in comps
                   for pr in programs
                   if pr.id_pc == pc.id]
    res_1 = sorted(one_to_many, key=itemgetter(3))  # Сортировка данных по операционной системе Компьютера
    print(res_1)

    print('Задание E2')
    res_2 = []
    for pc in comps:
        storage_usage_sum = sum([pr.storage_usage for pr in programs if (
                pr.id_pc == pc.id)])  # Считаем суммарно занимаемую программами память для каждого компьютера
        storage_usage_sum = round(storage_usage_sum, 1)  # Округляем до 1 знака после запятой
        res_2.append([pc.name, storage_usage_sum])  # Заполняем список новыми данными
        res_2 = sorted(res_2, key=itemgetter(1),  # Сортируем список относительно занимаемой памяти в порядке убывания
                       reverse=True)
    print(res_2)

    print('Задание E3')
    # Соединение данных много-ко-многим
    many_to_many_temp = [(pc.name, pc.os, pr_pc.id_prog)
                         for pc in comps
                         for pr_pc in prog_pc
                         if pc.id == pr_pc.id_pc
                         ]

    many_to_many = [(pr.name, pc_name, pc_os)
                    for pc_name, pc_os, prog_id in many_to_many_temp
                    for pr in programs if pr.id == prog_id
                    ]

    res_3 = {}
    for pc in comps:
        if 'Windows' in pc.os:
            pc_list = list(filter(lambda x: x[1] == pc.name, many_to_many)) # Из таблицы М-М достаем записи, свзяанные с текущим индексом цикла for
            prog_list = [prog_name for prog_name, pc_name, pc_os in pc_list] # Из полученных записей формируем список работабющих приложений для текущего индекса for
            res_3[pc.name] = prog_list
    print(res_3)


if __name__ == "__main__":
    main()
