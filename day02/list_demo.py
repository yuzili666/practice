alist = ['a', 4, 'nihao', '8', '就是', '哈']
blist = [1,2,3,4,5,6]

def list_sel():
    print(alist[0])
    print(alist[-1])
    print(len(alist))

    print(alist[0:])
    print(alist[-1:])
    print(alist[:])

    print(alist[-1::-1])

def list_del():
    alist.pop()
    print(alist)
    alist.pop(1)
    print(alist)

    blist = alist[0:2]
    print(blist)

def list_add():
    print(alist)
    alist.append('666')
    print(alist)
    alist.extend(blist)
    print(alist)
    alist.insert(-1,'nihao')
    print(alist)

def list_updata():
    alist[0] = 'yu'
    print(alist)

def list_look():
    alist[0] = 'yu'
    if 'yu' in alist:
        print('找到了')
    else:
        print('查无此人')

    if 'yu' not in alist:
        print('查无此人')
    else:
        print('有此人')


if __name__ == '__main__':
    list_sel()
    #  list_del()
    # list_add()
    # list_updata()
    # list_look()