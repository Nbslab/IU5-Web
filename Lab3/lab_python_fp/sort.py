data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def sort(data):
    return sorted(data, key=abs, reverse=True)

def sort_with_lambda(data):
    return sorted(data, key=lambda value: value if value > 0 else value*-1, reverse=True)

def main():
    print(str(sort(data))[1:-1])
    print(str(sort_with_lambda(data))[1:-1])

if __name__ == "__main__":
    main()