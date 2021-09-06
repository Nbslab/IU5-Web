#Lab1
#
#Solve biquadratic equation
#
#Задание решено с помощью классов, возможно будет изменяться, по ходу изучения языка
class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):
        return int(self.b)*int(self.b)-4*int(self.a)*int(self.c) #разбирался с конструкцией self

    def getSolve(self):
        num = self.getDiscriminant()
        if num<0:
            print("Решений нет")
        if num>=0:
            D = num ** (0.5)
            y1 = (((int(self.b))*(-1) + D)/2*int(self.a))
            y2 = (((int(self.b))*(-1) - D)/2*int(self.a))
            print("Y1 = " + str(y1))
            print("Y2 = " + str(y2))
            if (y1<0 and y2<0):
                print("Решений нет")
            if (y1==y2 and y1>=0):
                x1 = y1 ** (0.5)
                print("X1 = X2 = X3 = X4 =" + str(x1))
            if (y1!=y2):
                if (y1>0):
                    x1 = y1 ** (0.5)
                    print("X1 = " + str(x1) + " X2 = " + str(x1*(-1)))
                else:
                    print("Нет действительных корней X1, X2")
                if (y2>0):
                    x2 = y2 ** (0.5)
                    print("X3 = " + str(x2) + " X4 = " + str(x2*(-1)))
                else:
                    print("Нет действительных корней X3, X4")
        print("Незаметдинов Т.И. РТ5-51Б")

def main():
    a = input("Введите значение А: ")
    b = input("Введите значение B: ")
    c = input("Введите значение C: ")

    obj = Equation(a, b, c)
    obj.getSolve()

main()



