if __name__ == '__main__':
    list_x = [1, 2, 3, 4, 5, 6]
    list_y = [1, 2, 3, 4]
    list_z = [1, 0, 0, 1, 0, 1]


    def square(x):
        return x * x


    r = map(square, list_x)
    print(list(r))

    print('*' * 25)

    # 使用lambda表达式,充分发挥map的实力
    r1 = map(lambda x: x * x, list_x)
    print(list(r1))

    r2 = map(lambda x, y: x * x + y, list_x, list_y)
    print(list(r2))

    r3 = filter(lambda x: True if x == 1 else False, list_z)
    r4 = filter(lambda x: x, list_z)
    print(list(r3))
