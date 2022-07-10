import psycopg2
from psycopg2 import Error
import json
import os


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
        
        curs = conn.cursor()
        
        print("DB connected Sucessfully")
        curs.execute("select * from street_osm")
        fields= [desc[0] for desc in curs.description]
        for f in fields:
            print(f)
        return f

    except (Exception, Error) as error:
        print("Postgres Error: ", error)


def getColumn():
    '''return db fields'''










db=dbConnection()
print(db)

