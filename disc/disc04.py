def memory(n):
    x = n
    def update(f):
        nonlocal x
        x = f(x)
        print(x)
        return update
    return update

def add_this_many(x, el, lst):
    for i in range(len(lst)):
        if lst[i] == x:
            lst.append(el)

def reverse(lst):
    lenth = len(lst)
    for i in range(lenth//2):
        lst[i], lst[lenth - 1 - i] = lst[lenth - 1 - i], lst[i]

def group_by(s, fn):
    dic = dict()
    for elem in s:
        key = fn(elem)
        if key in dic:
            dic[key] += [elem]
        else:
            dic[key] = [elem]
    return dic

def replace_all_deep(d, x, y):
    for dic in d.values():
        for key, value in dic.items():
            if value == x:
                dic[key] = y
