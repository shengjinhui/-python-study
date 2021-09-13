if __name__ == '__main__':
    # 列表和元组的声明
    l = [1, 2, 'hello', 2]
    print(l)
    tup = ('json', 22, 22)
    print(tup)

    # 列表和元组添加元组
    # tup[1] = 20 这里会报错,python中元组是不可变的
    newTup = tup + (20,)
    print(newTup)

    l.append(5)
    print(l)

    # 列表与元组内置函数
    # 1. count(统计item在列表中出现的次数)
    print(l.count(2))
    print(l.count('hello'))
    print(l.count('hel'))

    print('...index...' * 10)
    # 2. index(返回元组在列表中第一次出现的索引)
    print(l.index(2))
    print(l.index(1))
    # print(l.index('hel')) 如果元素不存在,则会报错

    print('...reverse...' * 10)
    # 3. reverse
    l.reverse()
    print(l)
    newList = reversed(l)
    for _ in newList:
        print(_)

    # 4. sort
    # sort 只能支持同类型的元素之间的比较,eg: [1,'a',2,3,5] 就会抛异常 '<' not supported between instances of 'int' and 'str'
    intList = [2, 1, 5, 3, 5, 9, 7]
    intList.sort()
    print(intList)
    strList = ['a', 'z', 'b']
    strList.sort()
    print(strList)

    # 5. size
    print(intList.__len__())
    print(intList.__sizeof__())
