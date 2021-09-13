import openpyxl


# 这个类用来存储用例的
class Case:
    __slots__ = []
    pass


class ReadExcel(object):  # 读取excel数据的类
    def __init__(self, file_name, sheet_name):
        """
        :param file_name: 文件名 ---> str类型
        :param sheet_name: 表单名 ———> str类型
        """
        self.wb = openpyxl.load_workbook(file_name)
        self.sh = self.wb[sheet_name]

    def read_data_line(self):
        rows_data = list(self.sh.rows)
        titles = []
        for title in rows_data[0]:
            titles.append(title.value)
        cases = []
        for case in rows_data[1:]:
            data = []
            for cell in case:  # 获取一条测试用例数据
                data.append(str(cell.value))

            # 判断该单元格是否为字符串，如果是字符串类型则需要使用eval();如果不是字符串类型则不需要使用eval()将该条数据存放至cases中
            case_data = dict(list(zip(titles, data)))
            cases.append(case_data)
        return cases


if __name__ == '__main__':
    r = ReadExcel('未查询的店铺名称.xlsx', 'Sheet1')
    data1 = r.read_data_line()
    print(data1)
    l = list()
    for x in data1:
        l.append(x['店铺ID'])

    r2 = ReadExcel('test1.xlsx', 'Sheet1')
    data2 = r2.read_data_line()
    print(data2)

    l2 = list()
    for x in data2:
        l2.append(x['店铺id'])
    intersection = list(set(l).difference(set(l2)))
    print('*'*20)
    for x in intersection:
        print(x)
    print(len(intersection))
