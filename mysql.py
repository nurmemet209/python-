import pymysql

devdatabasename = "pppcar-supplier-dev"
prodatabasename = "pppcar-supplier"
devUrl = "rm-bp167v39m44a2ygxqo.mysql.rds.aliyuncs.com"
devUserName = "pppcar_dev"
devPassward = "pppcar2015Remuszpj"

proUrl = "rm-bp167v39m44a2ygxqo.mysql.rds.aliyuncs.com"
proUserName = "pppcar"
proPassward = "pppcar2015remuszpj"


def prn_obj(obj):
    print(['%s:%s' % item for item in obj.__dict__.items()])


# 获取数据库中所有的表
def getTables(cursor):
    tableList = []  # 列表List
    sql = "show tables"
    cursor.execute(sql)
    tls = cursor._rows
    for item in tls:
        tableList.append(item[0])  # item 是元祖 tuple 里面只包含一个元素即表名，取第一个
    return tableList


# 查询数据库中所有表的字段名 返回字典
def getAllTableColumnName(cursor):
    tableComlumsDic = {}  # 字典，{'表名称':[..字段列表...]}
    tableList = getTables(cursor)  # 查询所有表名称,返回列表List
    for item in tableList:
        columnList = []
        sql = "select * from " + item
        cursor.execute(sql)
        columnsDescrip = cursor.description  # (('id', 3, None, 11, 11, 0, False), ('slug', 253, None, 128, 128, 0, True), ('name', 253, None, 512, 512, 0, True), ('name_en', 253, None, 512, 512, 0, True))
        for colName in columnsDescrip:
            columnList.append(colName[0])
        tableComlumsDic[item] = columnList
    return tableComlumsDic


#
def getAll(host, username, passward, databasename):
    db = pymysql.connect(host, username, passward, databasename)
    cursor = db.cursor()
    columnsDic = getAllTableColumnName(cursor)
    db.close()
    return columnsDic


def compareColumns():
    devColumnDic = getAll(devUrl, devUserName, devPassward, devdatabasename)
    # devColumnDic={"test":['id','name','size','price']}
    proColumnDic = getAll(proUrl, proUserName, proPassward, prodatabasename)
    # proColumnDic={"test":['id','name','size']}
    for table, devColuList in devColumnDic.items():
        if table in proColumnDic:
            proColList = proColumnDic[table]
            missColList = list(set(devColuList).difference(set(proColList)))
            if len(missColList):
                print("生产环境缺少字段，表名：" + table)
                print("字段列表:")
                print(missColList)
        else:
            print("生产环境缺少表， 表名:" + table)


# compareColumns()





