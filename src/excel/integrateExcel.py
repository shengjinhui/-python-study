from src.util.excelUtil import ExcelUtil

if __name__ == '__main__':
    r = ExcelUtil('/Users/jhs/PycharmProjects/demo/resource/主播k级.xlsx', 'Sheet1')
    r2 = ExcelUtil('/Users/jhs/PycharmProjects/demo/resource/1.19商品进直播数据.xlsx', 'Sheet1')

    data1 = r.read_data_line()
    map1 = {}
    map2 = {}
    for d in data1:
        map1.setdefault(d['uname'], d['klevel'])
        map2.setdefault(d['klevel'], 0)

    noExistAnchorNum = 0
    for d in r2.read_data_line():
        anchorName = d['uname']
        print(anchorName)
        value = map1.get(anchorName)
        if value is None:
            noExistAnchorNum = noExistAnchorNum + 1
            continue
        sum = map2.get(value) + 1
        map2[value] = sum
        print("anchorName" + anchorName + "  " + value)

    print(map2)
    print(noExistAnchorNum)
