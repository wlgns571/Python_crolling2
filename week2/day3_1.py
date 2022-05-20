# 연산자 오버로딩
class NumBox:
    def __init__(self, num):
        self.num = num
    def __add__(self, others):
        print('다른객체', others.num)
        self.num += others.num

    def __sub__(self, num):
        self.num -= num
n = NumBox(10)
n2 = NumBox(100)
n + n2
print(n.num)
n - 50
print(n.num)
print(__name__)