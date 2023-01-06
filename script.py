from psycopg2 import Error, sql
from psycopg2.sql import SQL
import json
import os
import psycopg2


def getSetting():
    '''
    Info: reading setting from json file

    input: No input
    Output: JSON
    '''
    file = 'setting.json'
    fPath = os.path.join(os.getcwd(),file)
    oFile = open(fPath)
    readf = json.load(oFile)
    oFile.close()
    return readf

def getDbConnection(settings):
    '''connection to db data source'''
    dbconn = settings['DataBase']

    try:
        conn = psycopg2.connect(
            user = dbconn['User'],
            password = dbconn['Pass'],
            host = dbconn['Host'],
            port = dbconn['Port'],
            database = dbconn['DB'][0])
        
        if conn != None:
            curs = conn.cursor()
            return curs

    except (Exception, Error) as error:
        print("Postgres Error: ", error)


def getData(settings, cursor):
    '''return data from column'''
    tableName = settings['Data']['tableName'][0]
    searchField = settings['Data']['sarchField']

    queryStr = "SELECT {} FROM {} where {} is not null".format(searchField, tableName,searchField)
    cursor.execute(queryStr)
    searchData = cursor.fetchall()
    return [ d[0] for d in searchData]

    
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


class Node:
    def __init__(self,word = ''):
        self.word=word
        self.children=dict()
        self.endOfTxt = False

class Tree:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        current = self.root
        for i, char in enumerate(word): #noha
            #split 
            splitWord = word[0:i+1]
            if splitWord not in current.children: #check kol char in noha not exist in children of current node
                #insert char to child of node
                current.children[splitWord] = Node(splitWord)

                #print(current.children)     
            #update el current node
            current = current.children[splitWord]
        current.endOfTxt = True


    def search(self,word):
        current = self.root
        #split
        for i, char in enumerate(word):
            splitWord = word[0:i+1]
        #access childrens and check if char exist
            if splitWord in current.children:
               current = current.children[splitWord]

            else:
                print(word, 'IS not exist')
                return False

        if current.endOfTxt :
            return current.word
        else:
            print ('***** Suggestions******')
            return [key for key in current.children]



if __name__ == '__main__':
    settings = getSetting()
    cursor = getDbConnection(settings)
    data = getData(settings, cursor)
    t = Tree()
    for d in data:
        t.insert(d)
    print(t.search('Ra'))
