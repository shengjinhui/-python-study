def damage(skill1, skill2):
    damage1 = skill1 * 2
    damage2 = skill2 * 2 + 10
    return damage1, damage2


# 默认参数的使用
def print_student_info(name, gender='男', age=18, college='人民路小学'):
    print('my name is ' + name)
    print('my gender is ' + gender)
    print(' I am ' + str(age) + 'year old')
    print('I live in ' + college)


# 可变参数的使用
def add(*args):
    print(args)


# 关键字参数
def person(name, age, **kw):
    print('name:' + name + 'age:' + str(age) + 'other:' ,kw)


if __name__ == '__main__':
    # 处理元组的方式1
    damages = damage(1, 2)
    print(damages[0], damages[1])

    # 处理元组的方式2
    skill1_damage, skill2_damage = damage(2, 6)
    print(skill1_damage, skill2_damage)

    print_student_info('sjh', '女')

    add('a', 'b')
    person('sjh',18,city='北京',job='programmer')
