from random import randint
from timeit import timeit

if __name__ == '__main__':
    data = [randint(-10, 10) for _ in range(10)]
    print(list(randint(0, 10) for _ in range(20)))
    print(data)
    filter(lambda x: x >= 0, data)
    print('*' * 10)
    print(randint(0, 10))

    # 使用列表解析
    newData = [x for x in data if x >= 0]
    print(newData)

