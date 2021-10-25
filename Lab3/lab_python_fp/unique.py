from random import randint
from gen_random import  gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.index = 0
        self.data = list(items)
        self.unique_list = set()

        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration

            current = self.data[self.index]
            self.index += 1

            if self.ignore_case == True:
                if current not in self.unique_list:
                    if type(current) == str:
                        self.unique_list.add(current)
                        return current
                    else:
                        self.unique_list.add(current)
                        return current
            elif self.ignore_case == False:
                if type(current) == str:
                    if current.upper() not in self.unique_list and current.lower() not in self.unique_list:
                        self.unique_list.add(current.lower())
                        self.unique_list.add(current.upper())
                        return current
                else:
                    if current not in self.unique_list:
                        self.unique_list.add(current)
                        return current

    def __iter__(self):
        return self

data_int = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

def main():
    print(str(list(Unique(data_int)))[1:-1])
    print(str(list(Unique(data_str, ignore_case = True)))[1:-1])
    print(str(list(Unique(data_str, ignore_case = False)))[1:-1])
    print(str(list(Unique(gen_random(100, 1, 5))))[1:-1])

if __name__ == "__main__":
    main()
