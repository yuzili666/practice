alist = ['老王','老赵','东哥','老李','老余']

def for_demo():
    for i in range(5):
        print(i)
        print('helloworld')

def for_demo1():
    for i in range(3, 6):
        print(i,end='')
        print('helloworld')

def for_demo2():
    for i in range(0,6,2):
        print(i)

    for j in range(10,3,-2):
        print(j)

def bianli_demo():
    for i in alist:
        print(i)

def bianli2_demo():
    a = len(alist)
    for i in range(a):
        print(alist[i])

def for_qiantao():
    for i in range(5):
        print('XXX')
        for j in range(2):
            print('你好',end='')
        print()

def break_demo():
    for i in range(6):
        print(i)
        if i == 2:
            break

def continue_demo():
    for i in range(6):
        print(i)
        if i == 2:
            continue
        print('第%s次循环'%i)
        print()

if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    # for_demo2()
    # bianli_demo()
    # bianli2_demo()
    # for_qiantao()
    # break_demo()
    continue_demo()