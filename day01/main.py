def int_demo():
    aint = 5
    print(aint)
    print(type(aint))

def zhuanhaun_demo():
    aint = 7
    print(type(aint))
    print(type(str(aint)))
    print(type(float(aint)))

def str_join():
    a = 123
    b = '我爱'
    c = 'China'

    print(str(a)+b+c)
    print('a是%s，b是%s,c是%s'%(a,b,c))

def add_demo(a,b):
    print(a+b)

def jianfa_demo(a,b):
    c = a - b
    return c
if __name__ == '__main__':
    # int_demo()
    # zhuanhaun_demo()
    # str_join()
    # num = add_demo(5,3)
    # print(num)
    # num = jianfa_demo(8,3)
    # print(num)