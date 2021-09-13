class Student():
    name = ''
    age = 0

    def print_file(self):
        print('name is ' + self.name)
        print('age is ' + str(self.age))


if __name__ == '__main__':
    student = Student()
    student.print_file()


class Boy():
    name = ''
    age = 12

    def __init__(self, name):
        name = name

    def _init_(self, name, age):
        self.name = name
        self.age = age
