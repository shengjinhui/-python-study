import openpyxl


class ExcelUtil(object):
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
            # print(case)
            data = []
            for cell in case:
                data.append(str(cell.value))

            case_data = dict(list(zip(titles, data)))
            cases.append(case_data)
        return cases
