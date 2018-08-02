
def t1():
    x=2
    def f():
        print(x)
    return f


if __name__ == '__main__':
    a = t1()
    a()