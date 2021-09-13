if __name__ == '__main__':
    try:
        str = input("please enter two numbers:")
        num1 = int(str.split(',')[0].strip())
        num2 = int(str.split(',')[1].strip())

    except ValueError as err:
        print('Value Error: {}'.format(err))

    try:
        str = input("please enter two number:")
        num1 = int(str.split(',')[0].strip())
        num2 = int(str.strip(',')[0].strip())
    except ValueError as err:
        print('Value Error:{}'.format(err))
    except IndexError as err:
        print('Index Error:{}'.format(err))
    except Exception as err:
        print('UNKNOWN Error:{}'.format(err))
