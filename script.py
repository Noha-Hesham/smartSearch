from psycopg2 import Error, sql
from psycopg2.sql import SQL
import json
import os
import psycopg2


def readSetting():
    '''reading setting from json file'''
    file = 'setting.json'
    fPath = os.path.join(os.getcwd(),file)
    oFile = open(fPath)
    readf = json.load(oFile)
    return readf


def dbConnection():
    '''connection to db data source'''
    dbconn = readSetting()['DataBase']

    try:
        conn = psycopg2.connect(
            user = dbconn['User'],
            password = dbconn['Pass'],
            host = dbconn['Host'],
            port = dbconn['Port'],
            database = dbconn['DB'][0])
        
        if conn != None:
            curs = conn.cursor()
            print("DB connected Sucessfully")
            return curs

    except (Exception, Error) as error:
        print("Postgres Error: ", error)


def getData():
    '''return data from column'''
    tableName = readSetting()['Data']['tableName'][0]
    searchField = readSetting()['Data']['sarchField']
    connection = dbConnection()

#    query = "SELECT * FROM "
#    query += "{};".format(tableName)
#    connection.execute(query)
#    Data = connection.fetchall()
#
#    for d in Data:
#        '''list column data by column index'''
#        print (d[0])

    #---------------#

    queryStr = "SELECT {} FROM {} where {} is not null".format(searchField, tableName,searchField)
    connection.execute(queryStr)
    searchData = connection.fetchall()
    return [ d[0] for d in searchData]
    #for d in searchData:
    #    data = d[0]
    #    print(data)
#    for sd in searchData:
#        print(sd)
def creatListResultsFile():
    data = getData()
    filename = 'noha.text'
    with open(filename, "w") as file:
        file.write(str(data))
        path = os.path.join(os.getcwd(),filename)
        if os.path.exists(path) == True:
            return 'file ',filename, ' is created successfuly'
        else:
            return 'file',filename, 'is not exists successfuly'


class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]

    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


Data = ['Ring Road']
node = PrefixTree()
for i in Data :
    node.insert(i)
print(node.find('x'))