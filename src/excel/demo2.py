from src.util.excelUtil import ExcelUtil

if __name__ == '__main__':
    r = ExcelUtil('/Users/jhs/PycharmProjects/demo/resource/15161快速合作专区gmv统计.xlsx', 'Sheet1')
    r2 = ExcelUtil('/Users/jhs/PycharmProjects/demo/resource/快速合作专区1.15.xlsx', 'Sheet1')

    data1 = r.read_data_line()
    map1 = {}
    map2 = {}
    for d in data1:
        map1.setdefault(d['uname'], 0)
        # map2.setdefault(d['klevel'], 0)

    noExistAnchorNum = 0
    for d in r2.read_data_line():
        anchorName = d['uname']
        value = map1.get(anchorName)
        if value != 0:
            noExistAnchorNum = noExistAnchorNum + 1
            print(anchorName)
            continue

    print("no exist num", noExistAnchorNum)
