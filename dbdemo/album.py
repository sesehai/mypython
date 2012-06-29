# -*- coding:utf-8 -*-
'''
Created on 2012-6-24

@author: Administrator
'''

import db
import time

class Album(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.dbPython = {"host" : "127.0.0.1", "password" : "root", "username" : "root", "database" : "python"}

        
        
    def query(self, sql):
        cmyDb = self.getDbConnect(self.dbPython["host"],self.dbPython["password"],self.dbPython["username"],self.dbPython["database"])
        result = cmyDb.query(sql)
        return result
    
    def getDbConnect(self, host, user, password, dbname):
        cmyDb = db.CMySql()
        cmyDb.setoptions(host, user, password, dbname)
        cmyDb.start()
        return cmyDb
    def createAlbumJson(self):
        cmyDb = self.getDbConnect(self.dbAlbum["host"],self.dbAlbum["password"],self.dbAlbum["username"],self.dbAlbum["database"])
        sql = """SELECT 
        album.`id`,album.`name` 
        FROM 
        `album` as album,`rel_video_push` as rvp 
        WHERE 
        rvp.`rid`=album.`id` AND 
        rvp.`flag` = '1' AND 
        rvp.`pushflag` = '2' AND 
        album.`category` = '4' AND 
        album.`isdelete` <> '1' AND 
        album.`albumType`='1' 
        ORDER BY 
        album.`ctime`  
        DESC 
        LIMIT 
        0,50"""
        
        result = cmyDb.query(sql)
        return result

start = time.time()
album = Album()
#rows = album.query("select * from album order by id desc limit 5")

rows = album.createAlbumJson()
#print(rows)
for row in rows:
#    pass
    print(row[1])
#    print("\n")
end = time.time()
print(end - start)
    
