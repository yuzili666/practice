import json

adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":"123456"}'

def dict_sel():
    print(adict["username"])
    print(bdict[5])
    print(bdict["password"])

def dict_del():
    adict.pop('username')
    print(adict)
    print(bdict.pop(5))

def dict_updata():
    adict["username"] = '余自立'
    print(adict)

def dict_look():
    adict["username"] = '余自立'
    if '余自立' in adict:
        print('找到了')
    else:
        print('未找到')

def dict_add():
    adict.update(bdict)
    print(adict)

    dict = dict(adict, **bdict)
    print(dict)

def dict_add1():
    adict['sex'] = '男'
    print(adict)

def dict2str():
    str_adict = json.dumps(adict)
    print(type(str_adict))

def str2dict():
    cdict = json.loads(cdict_str)
    print(type(cdict))


if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_updata()
    # dict_look()
    # dict_add()
    # dict_add1()
    # dict2str()
    str2dict()